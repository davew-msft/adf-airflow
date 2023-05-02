# Using Apache Airflow with Azure Data Factory/Synapse Pipelines

[Managed Airflow documentation](https://learn.microsoft.com/en-us/azure/data-factory/concept-managed-airflow)

![](https://learn.microsoft.com/en-us/azure/data-factory/media/concept-managed-airflow/data-integration.png)

ADF is focused on "box-and-line"-style ELT development, whereas Airflow is a _python code-centric_ ETL tool.  

## Setup

1.  Spin up ADF 
2.  In ADF Studio, Manage, then Enable Airflow (choose Airflow 2)
3. Click on the Monitor link to start the airflow UI.  May also need to enable the ADF Preview Experience.  
4. You'll need a storage account with a container and a dags folder.  I have a public-facing one for testing:  
    * https://davewblob.blob.core.windows.net/airflow?sv=2021-10-04&st=2023-03-18T14%3A33%3A00Z&se=2024-04-19T14%3A33%3A00Z&sr=c&sp=rl&sig=mmJ9KTvEGeUDp9qtJoOWKGpy5zDymKlgYunYT8cXpSE%3D
5. Create an ADF linked service to that container
6. Choose Import to import the DAGs folder into managed airflow in ADF.  


## VSCode Extension

This would probably aid in development.  [Extension](https://marketplace.visualstudio.com/items?itemName=NecatiARSLAN.airflow-vscode-extension)

There are also a at least 3 other valuable airflow extensions if you search the marketplace for `airflow`.  

## Getting to Know Airflow

[Brief presentation](./airflow.pdf)  

[My Basic Example](./01BasicExample/README.md)  



## Useful Links

[Orchestrate and interop Astronomer and ADF](https://www.astronomer.io/integrations/microsoft-azure-data-factory/?utm_term=azure%20data%20factory%20airflow&utm_campaign=ch.sem_br.nonbrand_tp.prs_tgt.airflow-integrations_mt.xct_rgn.namer_lng.eng_dv.all_con.airflow-azure-data-factory&utm_source=google&utm_medium=sem&hsa_acc=4274135664&hsa_cam=18597872083&hsa_grp=146078064607&hsa_ad=628088531688&hsa_src=g&hsa_tgt=kwd-1832030292666&hsa_kw=azure%20data%20factory%20airflow&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=CjwKCAjw3POhBhBQEiwAqTCuBnwGhFnrhbVe2Uu2XMlQ4Khz6CTKz1F5dO5lo8v4xzS0jUHJb8mE8BoC8QgQAvD_BwE)



Needs:
* day in the life of a developer
* take a simple task, what does it look like in the new tech
* how do we do SDLC?  push to QA, test, productionize
* developers don't write a lot of sql (nodejs)
  * web-facing team.  responsible for bringing data into ecosystem
* currently tooling is vscode and ssms, but not docker
* "deletes" use case (on whiteboard)
* holy grail:  full file --> diff with whats out there --> change only the updates
  * currently done in SQL.  where else can it be done?  spark direct call to SQL?  can we do this in datalake and only push the updates to sql?  
  * how much data?  couple KB to multiple GBs
  * small feed is done this way, larger feed is done another way

Smaller 1-2 hour meeting is more helpful
* next:  spark notebooks, simple calculations.  notebooks with libraries, widgets, orchestrate from ADF or maybe even REST.  almost like the Seven Notebooks system.  
* next:  delete, joining feeds
* or:  airflow developer setup

goal:  how can we get dag to interop with whatever we do in the cloud?  tactical refactoring


  t1 = BashOperator(
    task_id='task_1',
    bash_command='/usr/bin/nodejs /usr/local/airflow/dags/test.js',
    dag=dag)