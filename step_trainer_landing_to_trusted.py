import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3  step trainer (landing zone)
S3steptrainerlandingzone_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://udacity-training-ab/project/step_trainer/landing/"],
        "recurse": True,
    },
    transformation_ctx="S3steptrainerlandingzone_node1",
)

# Script generated for node Curated customer data
Curatedcustomerdata_node1684746478980 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://udacity-training-ab/project/customer/curated/"],
        "recurse": True,
    },
    transformation_ctx="Curatedcustomerdata_node1684746478980",
)

# Script generated for node Join
Join_node1684746473060 = Join.apply(
    frame1=S3steptrainerlandingzone_node1,
    frame2=Curatedcustomerdata_node1684746478980,
    keys1=["serialNumber"],
    keys2=["serialNumber"],
    transformation_ctx="Join_node1684746473060",
)

# Script generated for node Drop Fields
DropFields_node1684746890790 = DropFields.apply(
    frame=Join_node1684746473060,
    paths=[
        "birthDay",
        "shareWithResearchAsOfDate",
        "registrationDate",
        "customerName",
        "email",
        "lastUpdateDate",
        "phone",
        "shareWithPublicAsOfDate",
        "shareWithFriendsAsOfDate",
    ],
    transformation_ctx="DropFields_node1684746890790",
)

# Script generated for node Trusted Trainer Records
TrustedTrainerRecords_node1684746928882 = glueContext.getSink(
    path="s3://udacity-training-ab/project/step_trainer/trusted/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="TrustedTrainerRecords_node1684746928882",
)
TrustedTrainerRecords_node1684746928882.setCatalogInfo(
    catalogDatabase="ab-udacity-project", catalogTableName="step_trainer_trusted"
)
TrustedTrainerRecords_node1684746928882.setFormat("json")
TrustedTrainerRecords_node1684746928882.writeFrame(DropFields_node1684746890790)
job.commit()
