# Checks for the presence of Crypto Currency mining scripts
# Written by Michael Skelton of NCC Group
# Forked with permission from session-tracking-checks.py
# which was authored by Brett Gervasoni of NCC Group

from burp import IBurpExtender
from burp import IScannerCheck
from burp import IScanIssue
from array import array

SOURCES = './lib/sources.txt'
with open(SOURCES) as f:
    sources = [s.strip() for s in f]

class BurpExtender(IBurpExtender, IScannerCheck):

    # implement IBurpExtender
    def registerExtenderCallbacks(self, callbacks):
        # keep a reference to our callbacks object
        self._callbacks = callbacks

        # obtain an extension helpers object
        self._helpers = callbacks.getHelpers()

        # set our extension name
        callbacks.setExtensionName("Minesweeper")

        # register ourselves as a custom scanner check
        callbacks.registerScannerCheck(self)

    # helper method to search a response for occurrences
    # of a literal match string
    # and return a list of start/end offsets
    def _get_matches(self, response, match):
        matches = []
        start = 0
        reslen = len(response)
        matchlen = len(match)
        while start < reslen:
            start = self._helpers.indexOf(response, match, False, start, reslen)
            if start == -1:
                break
            matches.append(array('i', [start, start + matchlen]))
            start += matchlen

        return matches

    # IScannerCheck
    def doPassiveScan(self, baseRequestResponse):
        issues = []

        # check for matches
        matches = []
        print("len(sources) = %d" % len(sources))
        print("*%s*" % sources[0])
        for source in sources:
            matches = self._get_matches(baseRequestResponse.getResponse(),
                                        self._helpers.stringToBytes(source))

            if len(matches) > 0:
                issues.append(CustomScanIssue(
                    baseRequestResponse.getHttpService(),
                    self._helpers.analyzeRequest(baseRequestResponse).getUrl(),
                    [self._callbacks.applyMarkers(baseRequestResponse,
                                                  None, matches)],
                    "Cryptocurrency mining script detected (cryptojacking)",
                    "Scripts were included from the following cryptocurrency mining domain: " + source,
                    "The web browsers of visitors to the website could be used to mine cryptocurrency without their knowledge.",
                    "Avoid using scripts from cryptocurrency mining domains. Cryptocurrency mining scripts are often added to a web page during a website compromise. Investigate whether unauthorised changes have been made to the web application.",
                    "High",
                    "Firm"))

        if (len(issues) == 0):
            return None

        # print("Found - "+str(self._helpers.analyzeRequest(baseRequestResponse).getUrl()))

        return issues

    def consolidateDuplicateIssues(self, existingIssue, newIssue):
        if existingIssue.getIssueName() == newIssue.getIssueName():
            return -1

        return 0


class CustomScanIssue (IScanIssue):
    def __init__(self, httpService, url, httpMessages, name, detail,
                 background, remediationBackground, severity, confidence):
        self._httpService = httpService
        self._url = url
        self._httpMessages = httpMessages
        self._name = name
        self._detail = detail
        self._background = background
        self._remediationBackground = remediationBackground
        self._severity = severity
        self._confidence = confidence

    def getUrl(self):
        return self._url

    def getIssueName(self):
        return self._name

    def getIssueType(self):
        return 0

    def getSeverity(self):
        return self._severity

    def getConfidence(self):
        return self._confidence

    def getIssueBackground(self):
        return self._background

    def getRemediationBackground(self):
        pass

    def getIssueDetail(self):
        return self._detail

    def getRemediationDetail(self):
        return self._remediationBackground

    def getHttpMessages(self):
        return self._httpMessages

    def getHttpService(self):
        return self._httpService
