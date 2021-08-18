from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 test_quality="",
                 expected_result="",
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.test_quality = test_quality
        self.expected_result = expected_result

    def execute(self, context):
       
        self.log.info("Getting credentials")
        redshift_hook = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        self.log.info("Testing data quality")
        records = redshift_hook.get_records(self.test_quality)
        if records[0][0] != self.expected_result:
            raise ValueError(f""" Data quality FAILURE. \
                The value: {records[0][0]} does not match the expected: {self.expected_result}
            """)
        else:
            self.log.info("Data quality PASS")