 
import os

# create directories for the project
os.makedirs('cloud_native_architecture', exist_ok=True)
os.makedirs('cloud_native_architecture/data_lake', exist_ok=True)
os.makedirs('cloud_native_architecture/lambda_functions', exist_ok=True)
os.makedirs('cloud_native_architecture/elastic_search', exist_ok=True)
os.makedirs('cloud_native_architecture/fast_api', exist_ok=True)
os.makedirs('cloud_native_architecture/great_expectations', exist_ok=True)

# create empty files for each directory
open('cloud_native_architecture/data_lake/raw_data.csv', 'a').close()
open('cloud_native_architecture/data_lake/processed_data.csv', 'a').close()
open('cloud_native_architecture/lambda_functions/lambda_function.py', 'a').close()
open('cloud_native_architecture/elastic_search/index_mappings.json', 'a').close()
open('cloud_native_architecture/fast_api/fast_api_app.py', 'a').close()
open('cloud_native_architecture/great_expectations/data_validation.yml', 'a').close()
