SELECT DISTINCT LineID, Line, EqPath FROM config.assets WHERE SiteID = :SiteID AND LineID != 0;