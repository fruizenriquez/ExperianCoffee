USE [DBExperianCoffee]
GO

/****** Object:  Table [dbo].[DimFarm]    Script Date: 7/07/2020 12:18:06 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[DimFarm](
	[Id] [int] NOT NULL PRIMARY KEY,
	[FarmName] [nvarchar](max) NULL,
	[CountryOfOrigin] [nvarchar](max) NULL,
	[Mill] [nvarchar](max) NULL,
	[Company] [nvarchar](max) NULL,
	[Region] [nvarchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

CREATE TABLE [dbo].[DimCertificate](
	[Id] [int] NOT NULL PRIMARY KEY,
	[CertificationBody] [nvarchar](max) NULL,
	[CertificationAddress] [nvarchar](max) NULL,
	[CertificationContact] [nvarchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

CREATE TABLE [dbo].[DimOwner](
	[Id] [int] NOT NULL PRIMARY KEY,
	[Owner] [nvarchar](max) NULL,
	[Phone] [nvarchar](max) NULL,
	[City] [nvarchar](max) NULL,
	[State] [nvarchar](max) NULL,
	[Zip] [nvarchar](max) NULL,
	[Country] [nvarchar](max) NULL,
	[Company] [nvarchar](max) NULL,
	[Title] [nvarchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

CREATE TABLE [dbo].[FactSample](
	[CertificateId] [int] FOREIGN KEY REFERENCES [DimCertificate](Id),
	[OwnerId] [int] FOREIGN KEY REFERENCES [DimOwner](Id),
	[FarmId] [int] FOREIGN KEY REFERENCES [DimFarm](Id),
	[LotNumber] [nvarchar](max) NULL,
	[ICONumber] [nvarchar](max) NULL,
	[Altitude] [float] NULL,
	[Producer] [nvarchar](max) NULL,
	[NumberOfBags] [int] NULL,
	[BagWeight] [nvarchar](max) NULL,
	[InCountryPartner] [nvarchar](max) NULL,
	[HarvestYear] [nvarchar](max) NULL,
	[Grading] [datetime] NULL,
	[Variety] [nvarchar](max) NULL,
	[Status] [nvarchar](max) NULL,
	[ProcessingMethod] [nvarchar](max) NULL,
	[Aroma] [float] NULL,
	[Flavor] [float] NULL,
	[Aftertaste] [float] NULL,
	[Acidity] [float] NULL,
	[Body] [float] NULL,
	[Balance] [float] NULL,
	[Uniformity] [float] NULL,
	[CleanCup] [float] NULL,
	[Sweetness] [float] NULL,
	[Overall] [float] NULL,
	[Defects] [int] NULL,
	[TotalCupPoints] [float] NULL,
	[Moisture] [float] NULL,
	[CategoryOneDefects] [int] NULL,
	[Quakers] [int] NULL,
	[Color] [nvarchar](max) NULL,
	[CategoryTwoDefects] [int] NULL,
	[Expiration] [datetime] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
