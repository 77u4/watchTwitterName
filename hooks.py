#
# Copyright (c) 2008-2010 Thomas Perl <thp@thpinfo.com>
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. The name of the author may not be used to endorse or promote products
#    derived from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#


# You can decide which filter you want to apply using the "url"
# parameter and you can use the "re" module to search for the
# content that you want to filter, so the noise is removed.


# Needed for regular expression substitutions
import re

# Additional modules installed with urlwatch
from urlwatch import ical2txt
from urlwatch import html2txt


def filter(url, data):
    if url.startswith('https://twitter.com/'):
        return re.sub('<input type="hidden" name="authenticity_token" value=".*">', '', 
        		re.sub('<input type="hidden" id="init-data" class="json-data" value=".*">', '', 
        		 re.sub('<input type="hidden" value=".*" name="authenticity_token"\/>', '', 
				  re.sub('<link .*>','',
				   re.sub('background-image: url\(https\:\/\/.*\);', '', data)))))
				   
    elif url.endswith('.ics') or url == 'http://www.kukuk.at/ical/events':
        # example of generating a summary for icalendar files
        # append "data" to the converted ical data, so you get
        # all minor changes to the ICS that are not included
        # in the ical2text summary (remove this if you want)
        return ical2txt.ical2text(data).encode('utf-8') + '\n\n' + data
    elif url == 'http://www.oho.at/programm/programm.php3':
        # example of converting HTML to plaintext for very
        # ugly HTML code that cannot be deciphered when just
        # diffing the HTML source (or if the user is just not
        # used to HTML, use this for every web page)
        #
        # You need to install "lynx" for this to work or use
        # "html2text" as method (needs "html2text") or use
        # "re" (does not need anything, but only strips tags
        # using a regular expression and does no formatting)
        return html2txt.html2text(data, method='lynx')
    return data


