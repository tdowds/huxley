# Copyright (c) 2011-2013 Kunal Mehta. All rights reserved.
# Use of this source code is governed by a BSD License found in README.md.

from django.shortcuts import render_to_response
from django.template import RequestContext

def render_template(request, template, context=None):
    """ Wrapper around render_to_response that sets context_instance. """
    return render_to_response(template, context, 
                              context_instance=RequestContext(request))