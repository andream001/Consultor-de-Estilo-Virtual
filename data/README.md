# Datasets Information
# ===================

## H&M Dataset Structure
- **articles.csv**: Product information
- **customers.csv**: Customer demographics  
- **transactions_train.csv**: Purchase history

## Rent the Runway Dataset Structure
- **renttherunway_final_data.json**: Fit and sizing data

## Sample Data
Sample datasets are created automatically when running the data collection scripts.
The sample data maintains the same structure as the original datasets but with 
a smaller number of records for development and testing purposes.

## Data Processing Pipeline
1. **Collection**: Download or create sample data
2. **Cleaning**: Handle missing values, standardize formats
3. **Integration**: Combine datasets into hybrid structure
4. **Feature Engineering**: Create new variables for modeling
5. **Export**: Save processed data in multiple formats