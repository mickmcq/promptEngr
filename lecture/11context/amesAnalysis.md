# Ames Housing 2011 - Comprehensive Data Analysis

## Dataset Overview
- **2,925 properties** with **82 features** describing various aspects of homes in Ames, Iowa
- Mix of numerical (39) and categorical (43) variables

## Data Structure

### Rows and Columns
- Rows: 2,925
- Columns: 82

### Column Types
- **Numerical columns**: 39 features (int64, float64)
- **Categorical columns**: 43 features (object)

## Sale Price Statistics

### Summary Statistics
- **Average sale price**: $180,412
- **Median**: $160,000
- **Standard deviation**: $78,555 (indicating considerable price variation)
- **Minimum**: $12,789
- **25th percentile**: $129,500
- **75th percentile**: $213,500
- **Maximum**: $625,000

## Data Quality Analysis

### Missing Data
- **Overall**: 15,732 missing values (6.56% of total data)

### Missing Values by Column (Top Issues)
| Column | Missing Count | Percentage |
|--------|--------------|------------|
| PoolQC | 2,914 | 99.6% |
| MiscFeature | 2,820 | 96.4% |
| Alley | 2,727 | 93.2% |
| Fence | 2,354 | 80.5% |
| MasVnrType | 1,774 | 60.6% |
| FireplaceQu | 1,422 | 48.6% |
| LotFrontage | 490 | 16.8% |
| GarageType | 157 | 5.4% |
| GarageYrBlt | 159 | 5.4% |
| GarageFinish | 159 | 5.4% |
| GarageQual | 159 | 5.4% |
| GarageCond | 159 | 5.4% |
| BsmtQual | 80 | 2.7% |
| BsmtCond | 80 | 2.7% |
| BsmtExposure | 83 | 2.8% |
| BsmtFinType1 | 80 | 2.7% |
| BsmtFinType2 | 81 | 2.8% |

**Note**: High missing percentages for PoolQC, MiscFeature, Alley, and Fence likely indicate that most homes don't have these features rather than true missing data.

## Strongest Predictors of Sale Price

Based on correlation analysis, the most important factors for predicting sale price:

| Feature | Correlation | Description |
|---------|-------------|-------------|
| OverallQual | 0.81 | Overall quality rating |
| GrLivArea | 0.72 | Above ground living area (sq ft) |
| TotalBsmtSF | 0.66 | Total basement square footage |
| GarageCars | 0.65 | Garage capacity (number of cars) |
| GarageArea | 0.65 | Garage size (sq ft) |
| 1stFlrSF | 0.64 | First floor square footage |
| YearBuilt | 0.57 | Original construction year |
| YearRemod/Add | 0.54 | Remodel year |
| FullBath | 0.54 | Number of full bathrooms |
| GarageYrBlt | 0.53 | Year garage was built |
| MasVnrArea | 0.51 | Masonry veneer area |
| TotRmsAbvGrd | 0.50 | Total rooms above grade |
| Fireplaces | 0.47 | Number of fireplaces |
| BsmtFinSF1 | 0.44 | Type 1 finished basement area |

## Property Characteristics

### Zoning Distribution (MSZoning)
- **RL** (Residential Low Density): 2,268 (77.5%)
- **RM** (Residential Medium Density): 462 (15.8%)
- **FV** (Floating Village Residential): 139 (4.8%)
- **RH** (Residential High Density): 27 (0.9%)
- **C (all)** (Commercial): 25 (0.9%)
- **I (all)** (Industrial): 2 (0.1%)
- **A (agr)** (Agriculture): 2 (0.1%)

### Street Type
- **Pave**: 2,913 (99.6%)
- **Grvl** (Gravel): 12 (0.4%)

### Lot Shape
- **Reg** (Regular): 1,859 (63.6%)
- **IR1** (Slightly Irregular): 975 (33.3%)
- **IR2** (Moderately Irregular): 76 (2.6%)
- **IR3** (Irregular): 15 (0.5%)

### Land Contour
- **Lvl** (Level): 2,631 (89.9%)
- **HLS** (Hillside): 120 (4.1%)
- **Bnk** (Banked): 114 (3.9%)
- **Low** (Depression): 60 (2.1%)

## Sales Timeline
- **Years covered**: 2006-2010
- Properties show slight negative correlation with order/time (-0.03)

## Key Insights

1. **Quality is King**: Overall quality rating has the strongest correlation (0.81) with sale price, making it the single best predictor.

2. **Size Matters**: Living area (GrLivArea), basement size (TotalBsmtSF), and first floor size (1stFlrSF) are all strong predictors, indicating that larger homes command higher prices.

3. **Garage Value**: Both garage capacity and size show strong correlations (0.65), suggesting that garage features are highly valued by buyers.

4. **Age Factor**: Year built (0.57) and remodel year (0.54) show moderate positive correlations, indicating newer or recently renovated homes sell for more.

5. **Missing Data Pattern**: The high percentage of missing values for PoolQC (99.6%), MiscFeature (96.4%), and Alley (93.2%) likely reflects that most properties simply don't have these features rather than data collection issues.

6. **Market Composition**: The market is dominated by residential low-density properties (77.5%), with nearly all properties having paved streets (99.6%) and level land (89.9%).

## Visualizations Generated
- **correlation_heatmap.png** - Shows relationships between numerical variables
- **distributions.png** - Displays distributions of key numerical features
- **categorical_distributions.png** - Shows frequency of categorical variables

## Use Case
This dataset is commonly used for:
- Predictive modeling of house prices
- Feature importance analysis in real estate
- Machine learning regression tasks
- Understanding factors that drive property values in midwest American markets
