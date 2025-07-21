# simple_pyspark_job_with_dbx
Running a PySpark job with a DBX Notebook, and then submitting to the Jobs API


Step 1 - Create a Git Folder within Databricks (using this repository)

Step 2 - Open the Notebook (FirstNotebook.ipynb)
```
Change the catalog "cicak_tester" to your catalog, and the schema "default" to your schema. 
```
Step 3 - Run the Notebook in Serverless


-----
Create a job and run the job via the REST API:

Step 4 - After your ran your first notebook, go to the Catalog to validate the table was created under catalog > schema > test_table

Step 5 - Go to User Icon at top right > Settings > User > Developer > Access tokens & Generate a new token (save your token)

Step 6 - Create a file locally on your Desktop called create-job.json (change youremail@address.com to your email)
```
{
  "name": "Serverless Example Job",
  "environments": [
    {
      "environment_key": "default",
      "spec": {
        "client": "3",
        "dependencies": []
      }
    }
  ],
  "tasks": [
    {
      "task_key": "simple_pyspark_job",
      "spark_python_task": {
        "python_file": "/Users/youremail@address.com/simple_pyspark_job_with_dbx/myjob.py"
      },
      "environment_key": "default"
    }
  ]
}
```


Step 7 - Run the following command in a Terminal (referencing the create-job.json on your Desktop) - save the job id
```
curl -X POST https://yourdbc-endpoint/api/2.1/jobs/create \
  -H "Authorization: Bearer YOURTOKEN" \
  -H "Content-Type: application/json" \
  -d @create-job.json

```

Step 8 - Run the job id (from Step 7)
```
curl -X POST https://yourdbc-endpoint/api/2.1/jobs/run-now \
  -H "Authorization: Bearer YOURTOKEN" \
  -H "Content-Type: application/json" \
  -d '{"job_id": 742251434665239}'
```
