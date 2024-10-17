from typing import NamedTuple
from xetra.common.s3 import S3BucketConnector
import logging

class XetraSourceConfig(NamedTuple):
    """
    Class for columns and dates for xetra data
    """
    src_first_extract_date: str
    src_columns: list
    src_first_station: str
    src_second_station: str
    src_first_element: str
    src_second_element: str
    src_first_date: str
    src_second_date: str
    src_value: str
    
class XetraTargetConfig(NamedTuple):
    """
    Class for columns and dates for xetra data
    """
    trg_first_extract_date: str
    trg_columns: list
    trg_first_station: str
    trg_second_station: str
    trg_first_element: str
    trg_second_element: str
    trg_first_date: str
    trg_second_date: str
    trg_value: str
    
    
class XetraETL():
    """
    Reads xetra data from S3, transforms 
    it and writes it back to S3
    """  
    
    def __init__(self, s3_bucket_src: S3BucketConnector,
                 s3_bucket_trg: S3BucketConnector,
                 meta_key: str,
                 src_args: XetraSourceConfig,
                 trg_args: XetraTargetConfig):
        
        self._logger = logging.getLogger(__name__) 
        self.s3_bucket_src = s3_bucket_src
        self.s3_bucket_trg = s3_bucket_trg
        self.meta_key = meta_key
        self.src_args = src_args
        self.trg_args = trg_args
        self.extract_date = 
        self.extract_date_list = 
        self.meta_update_list = 
        
    def extract(self):
        pass
    
    def transform_report1(self):
        pass
    
    def load(self):
        pass
    
    def etl_report1(self):
        pass