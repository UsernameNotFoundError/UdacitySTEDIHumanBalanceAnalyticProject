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

# Script generated for node customer trusted
customertrusted_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://udacity-training-ab/project/customer/trusted/"],
        "recurse": True,
    },
    transformation_ctx="customertrusted_node1",
)

# Script generated for node accelerometer trusted
accelerometertrusted_node1684740787398 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://udacity-training-ab/project/accelerometer/trusted/"],
        "recurse": True,
    },
    transformation_ctx="accelerometertrusted_node1684740787398",
)

# Script generated for node Join
Join_node1684740790418 = Join.apply(
    frame1=accelerometertrusted_node1684740787398,
    frame2=customertrusted_node1,
    keys1=["user"],
    keys2=["email"],
    transformation_ctx="Join_node1684740790418",
)

# Script generated for node Drop Fields
DropFields_node1684741003725 = DropFields.apply(
    frame=Join_node1684740790418,
    paths=["x", "y", "user", "timeStamp", "z"],
    transformation_ctx="DropFields_node1684741003725",
)

# Script generated for node customer curated
customercurated_node1684741239972 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1684741003725,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://udacity-training-ab/project/customer/curated/",
        "partitionKeys": [],
    },
    transformation_ctx="customercurated_node1684741239972",
)

job.commit()
