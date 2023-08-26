# Datathon Scor 2023: Team 07


The challenge was about predicting the Environmental impact of companies based on their properties like Industry, Region, CO2 Emissions,...

Some functions used in this notebook are defined in separate Python files to make our code as clear as possible, these files are: preprocessing.py, processing.py and Labels.py

In our study, we followed the steps below to generate our predictions on EnvRatingNumeric and EnvRating.

# Part 1: Data preparation 

## First drops
We begin our study by dropping unnecessary columns, which are columns that:
- Do not exist in the test set
- Do not provide meaningful information
- Do not provide extra information (there exist other columns that provide approximatly the same information)
- Single valued

## PrimarySector and GICSSector and PrimaryIndustry and GICSSubIndustry:

Then we start filling categorical missing values for the columns GICSSector and GICSSubIndustry, using the columns PrimaryIndustry and primarySector respectively, while trying to conserve as much as possible the convention of GICS.

## Merge:

Here, we merge the columns (enriching data) ClimateEmissionsReportedTrust and ClimateEmissionsestimatedTrust because they give the same information, the only difference is that their values are gotten differently.

## Web searching:

After, we tried to fill the missing values (approximatly 18 rows) of GICSSector and GICSSubIndustry for the test set using our research on the web (collecting data).


## Filling Missing values for non-categorical features
In this subsection, we moved on to fill the numeric missing values using means but applied on data that belong to the same GICSSubIndustry or GICSSector.(Clustering technique)

## Dealing with the remaining features:
Here, we drop rows with missing values since there are so little, and we drop also the column 'CompanyNameAlias' since we will not use it anymore (we used it in the function match_subIndustry).

# Part 2: Data visualization:

## Univariate Analysis:
We start by a univarite analysis to determine if there are columns that are very correlated to each other or not, and we found that it was the case for ClimateTotalEmissions with ClimateScope1Emissions (which was expected since the total = scope1 + scope2) and for MarketCap and CompanyValue (which was also expected because the company value is its Market cap along with debts, claimants, cash equivalent, etc). The surprising part is that these relations appear to be linear in our dataset !

## Outliers:
We did some boxplots to determine whether there are some outliers or not. Then we dropped some of them.

# Part 3: Modeling Catboost:

## Parameters:

In this section, we used CatBoost Regressor, which is a gradient boosting algorithm, to predict our test set. We chose the parameters that give the best performances which are:
- iterations = 5000
- learning_rate = default
- depth = 6
- loss_function = MAE
- l2_leaf_reg = 1

## Evaluate the model:

We evaluated our model using cross-validation, and it gives an error of approximatly 0.23

## Final submission:
 After validating the performances of our model, we computed the final predictions.

 # Analysis of the model:

 Using the library shap, and some other tools, we plot some figures that interpret our model like the feaure importances.

 # End 