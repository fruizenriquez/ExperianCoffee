--****************************
/*Marcio preference*/
--****************************
SELECT 	TOP 100
		DimOwner.Owner,
		DimOwner.Country,
		DimOwner.State,
		DimFarm.FarmName,
		DimFarm.Region,
		FactSample.*

FROM	FactSample
		INNER JOIN DimCertificate ON DimCertificate.Id = FactSample.CertificateId
		INNER JOIN DimOwner ON DimOwner.Id = FactSample.OwnerId
		INNER JOIN DimFarm ON DimFarm.Id = FactSample.FarmId

WHERE	DimOwner.Country IN('Brazil')
AND		DimFarm.Region IN('Sul De Minas')

--****************************
/*Subu preference*/
--****************************
SELECT 	TOP 100
		DimOwner.Owner,
		DimOwner.Country,
		DimOwner.State,
		DimFarm.FarmName,
		DimFarm.Region,
		FactSample.*

FROM	FactSample
		INNER JOIN DimCertificate ON DimCertificate.Id = FactSample.CertificateId
		INNER JOIN DimOwner ON DimOwner.Id = FactSample.OwnerId
		INNER JOIN DimFarm ON DimFarm.Id = FactSample.FarmId

WHERE	FactSample.Sweetness = (SELECT MAX(FactSample.Sweetness)
								FROM FactSample)
AND		FactSample.Flavor = (SELECT MIN(FactSample.Flavor)
								FROM FactSample)