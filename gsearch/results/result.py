import gsearch.errors.resultErrors as resultErrors
import json

class result():
    #google search result
    def __init__(self, title=None, url=None, description=None, place=None, header=None, query=None):
        """
        Google search result object. This class is for a single result.
        
        Most parameters, with the exception of description are required.
        
        Parameters
        ----------
        @title: The title or header given when the result was found. Defaults to `None`, although **this raises an error**.
        
        @url: The url corresponding to the title given when the result was found. Defaults to `None`, although **this raises an error**.
        
        @description: The description corresponding to the title given when the result was found. Defaults to `None`, this does not raise an error.
        
        @header: The header used, or search agent used. Added manually by the scraper for debugging purposes. Does not raise an error.
        
        @query: The query specified, or what was searched. Added manually by the scraper for debugging purposes. Does not raise an error.
        
        Raises
        ------
        `resultErrors.InvalidResult`: Raised when title or url are `None`.
        """
        self.title = title
        self.url = url
        self.description = description
        self.place = place
        self._runSelfChecks()
        # DEBUG PARAMETERS
        self.header = header
        self.query = query
        
    def _runSelfChecks(self):
        # check for attrubutes
        if self.title == None:
            raise resultErrors.InvalidResult(f"Title is {self.title}")
        if self.place == None:
            raise resultErrors.InvalidResult(f"Place is {self.place}")
        if self.url == None:
            raise resultErrors.InvalidResult(f"URL is {self.url}")
        
    def toJson(self):
        """
        Returns a JSON representation of the result object.
        
        Returns
        -------
        `str`: JSON representation of the result object.
        """
        returns = {"title": "{self.title}", 
                    "url": "{self.url}", 
                    "description": "{self.description}", 
                    "place": "{self.place}"
                } 
                   
        return json.dumps(returns)
    def debugVariables(self):
        return self.header, self.query