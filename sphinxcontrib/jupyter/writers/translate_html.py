"""
Translator to Support IPYNB(HTML) and Website Support
"""

from __future__ import unicode_literals
import re
import nbformat.v4
from docutils import nodes, writers
from shutil import copyfile
import copy
import os

from .translate_ipynb import JupyterIPYNBTranslator
from .utils import JupyterOutputCellGenerators
from .notebook import JupyterNotebook
from .html import HTMLSyntax

class JupyterHTMLTranslator(JupyterIPYNBTranslator):


    def __init__(self, document, builder):
        """ 
        Jupyter Translator for HTML End Target Support

        This will generate IPYNB files emphasis on HTML that are 
        built to work with the `nbconvert` template to support website 
        construction
        """
        super().__init__(document, builder)
        # HTML Settings
        self.html_ext = ".html"
        self.syntax = HTMLSyntax()

    #-Nodes-#

    def visit_image(self, node):
        """
        Image Directive
        Include Images as HTML including attributes that  
        are available from the directive
        """
        uri = node.attributes["uri"]
        self.images.append(uri)
        attrs = node.attributes
        self.cell.append(self.syntax.visit_image(uri, attrs))

    def visit_label(self, node):
        if self.footnote['in']:
            ids = node.parent.attributes["ids"]
            id_text = ""
            for id_ in ids:
                id_text += "{} ".format(id_)
            else:
                id_text = id_text[:-1]

            self.cell.append("<p><a id={} href=#{}-link><strong>[{}]</strong></a> ".format(id_text, id_text, node.astext()))
            raise nodes.SkipNode

        if self.citation['in']:
            self.cell.append(self.syntax.visit_label())

    #References(Start)

    def depart_reference(self, node):
        subdirectory = False

        if self.topic:
            # Jupyter Notebook uses the target text as its id
            uri_text = "".join(
                self.cell[self.reference_text_start:]).strip()
            uri_text = re.sub(
                self.URI_SPACE_REPLACE_FROM, self.URI_SPACE_REPLACE_TO, uri_text)
            uri_text = uri_text.replace("(", "%28").replace(")", "%29")
            self.in_reference['uri_text'] = uri_text
            formatted_text = "](#{})".format(self.reference['uri_text'])
            self.cell.append(formatted_text)
        else:
            # if refuri exists, then it includes id reference
            if "refuri" in node.attributes:
                refuri = node["refuri"]
                # add default extension(.ipynb)
                if "internal" in node.attributes and node.attributes["internal"] == True:
                    refuri = self.add_extension_to_inline_link(refuri, self.html_ext)
            else:
                # in-page link
                if "refid" in node:
                    refid = node["refid"]
                    self.inpage_reference = True
                    #markdown doesn't handle closing brackets very well so will replace with %28 and %29
                    #ignore adjustment when targeting pdf as pandoc doesn't parse %28 correctly
                    refid = refid.replace("(", "%28")
                    refid = refid.replace(")", "%29")
                    #markdown target
                    refuri = "#{}".format(refid)
                # error
                else:
                    self.error("Invalid reference")
                    refuri = ""

            #TODO: review if both %28 replacements necessary in this function?
            #      Propose delete above in-link refuri
            #ignore adjustment when targeting pdf as pandoc doesn't parse %28 correctly
            refuri = refuri.replace("(", "%28")  #Special case to handle markdown issue with reading first )
            refuri = refuri.replace(")", "%29")
            if self.List:
                marker = self.List.get_marker()
                text = "]({})".format(refuri)
                self.List.add_item(text)
            else:
                self.cell.append("]({})".format(refuri))

        if self.toctree:
            self.cell.append("\n")

    def visit_footnote_reference(self, node):
        self.footnote_reference['in'] = True
        refid = node.attributes['refid']
        ids = node.astext()
        self.footnote_reference['link'] = "<sup><a href=#{} id={}-link>[{}]</a></sup>".format(refid, refid, ids)
        self.cell.append(self.footnote_reference['link'])
        raise nodes.SkipNode

    #References(End)
