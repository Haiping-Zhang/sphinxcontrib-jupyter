import nbformat
from nbconvert import PDFExporter
from nbconvert import LatexExporter
import os
import sys
from io import open
import subprocess
from sphinx.util.osutil import ensuredir
from sphinx.util import logging
from nbconvert.preprocessors import LatexPreprocessor
from distutils.dir_util import copy_tree
from .process_latex import main as latexProcessing 

class MakePdfWriter():
    """
    Makes pdf for each notebook
    """
    logger = logging.getLogger(__name__)
    def __init__(self, builderSelf):
        self.pdfdir = builderSelf.outdir + "/pdf" #pdf directory 
        self.texdir = builderSelf.outdir + "/executed" #latex directory 

        for path in [self.pdfdir, self.texdir]:
            ensuredir(path)

        self.pdf_exporter = PDFExporter()
        self.tex_exporter = LatexExporter()

    def convertToLatex(self, builderSelf, filename):
        """
        function to convert notebooks to latex
        """
        relative_path = ''
        tex_data = ''
        tex_build_path = self.texdir + relative_path
        pdf_build_path = self.pdfdir + relative_path

        ensuredir(tex_build_path)
        ensuredir(pdf_build_path)

        ## setting the working directory
        os.chdir(self.texdir)

        ## copies all theme folder images to static folder
        if os.path.exists(builderSelf.confdir + "/theme/static/img"):
            copy_tree(builderSelf.confdir + "/theme/static/img", builderSelf.executed_notebook_dir + "/_static/img/", preserve_symlinks=1)
        else:
            self.logger.warning("Theme folder not present. Consider creating a theme folder for static assets")

        fl_ipynb = builderSelf.executed_notebook_dir + "/" + "{}.ipynb".format(filename)
        fl_tex = builderSelf.executed_notebook_dir + "/" + "{}.tex".format(filename)

        fl_tex_template = builderSelf.confdir + "/" + builderSelf.config['jupyter_latex_template']

        ## do not convert index and zreferences to latex
        if filename.find('index') == -1 and filename.find('zreferences') == -1:  
            ## --output-dir - forms a directory in the same path as fl_ipynb - need a way to specify properly?
            ### converting to pdf using xelatex subprocess
            subprocess.run(["jupyter", "nbconvert","--to","latex","--template",fl_tex_template,"from", fl_ipynb])
            latexProcessing(self, fl_tex)
            try:
                self.subprocessXelatex(fl_tex, filename)
                self.subprocessBibtex(filename)
                self.subprocessXelatex(fl_tex, filename)
                self.subprocessXelatex(fl_tex, filename)
            except OSError as e:
                print(e)
            except AssertionError as e:
                pass
                # exit() - to be used when we want to execution to stop on error

    def subprocessXelatex(self, fl_tex, filename):
        p = subprocess.Popen(("xelatex", "-interaction=nonstopmode", fl_tex), stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        output, error = p.communicate()
        if (p.returncode != 0):
            self.logger.warning('xelatex exited with returncode {} , encounterd in {} with error -- {}'.format(p.returncode , filename, error))

        # assert (p.returncode == 0), self.logger.warning('xelatex exited with returncode {} , encounterd in {} with error -- {}'.format(p.returncode , filename, error)) ---- assert statement stops the program, will handle it later

    def subprocessBibtex(self, filename):
        p = subprocess.Popen(('bibtex',filename), stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        output, error = p.communicate()
        if (p.returncode != 0):
            self.logger.warning('bibtex exited with returncode {} , encounterd in {} with error -- {} {}'.format(p.returncode , filename, output, error))
        
        # assert (p.returncode == 0), self.logger.warning('bibtex exited with returncode {} , encounterd in {} with error -- {} {}'.format(p.returncode , filename, output, error)) ---- assert statement stops the program, will handle it later
