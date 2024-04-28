'''
Farzana Ahamed Bhuiyan 
Dec 3, 2020
Report Frequency: RQ2
'''
'''
Forensics added by Alden Snajder
'''
import numpy as np 
import os 
import pandas as pd 
import time 
import datetime 
import statistics
import myLogger

def giveTimeStamp():
  tsObj = time.time()
  strToret = datetime.datetime.fromtimestamp(tsObj).strftime( '%Y-%m-%d %H:%M:%S' ) 
  return strToret

def Average(Mylist): 
    return sum(Mylist) / len(Mylist)
    
def Median(Mylist): 
    return statistics.median(Mylist)
    
def reportProp( res_file ):
    res_df = pd.read_csv(res_file) 
    fields2explore = ['DATA_LOAD_COUNT', 'MODEL_LOAD_COUNT', 'DATA_DOWNLOAD_COUNT',	'MODEL_LABEL_COUNT', 'MODEL_OUTPUT_COUNT',	
                      'DATA_PIPELINE_COUNT', 'ENVIRONMENT_COUNT', 'STATE_OBSERVE_COUNT',  'TOTAL_EVENT_COUNT'
                     ]
                     
    for field in fields2explore:
        field_res_list = res_df[res_df['CATEGORY'] == field ]   
        prop_val_list = field_res_list['PROP_VAL'].tolist() 
        print(prop_val_list)
        average_prop_metric = Average(prop_val_list)        
        print('CATEGORY:{}, AVG_PROP_VAL:{}'.format( field, average_prop_metric  ))
        print('-'*50)     
        median_prop_metric = Median(prop_val_list)        
        print('CATEGORY:{}, MEDIAN_PROP_VAL:{}'.format( field, median_prop_metric  ))
        print('-'*50)          
    
    
def reportDensity( res_file ):
    res_df = pd.read_csv(res_file) 
    fields2explore = ['DATA_LOAD_COUNT', 'MODEL_LOAD_COUNT', 'DATA_DOWNLOAD_COUNT',	'MODEL_LABEL_COUNT', 'MODEL_OUTPUT_COUNT',	
                      'DATA_PIPELINE_COUNT', 'ENVIRONMENT_COUNT', 'STATE_OBSERVE_COUNT',  'TOTAL_EVENT_COUNT'
                     ]
                     
    for field in fields2explore:
        field_res_list = res_df[res_df['CATEGORY'] == field ]   
        density_val_list = field_res_list['EVENT_DENSITY'].tolist() 
        average_density_metric = Average(density_val_list)        
        print('CATEGORY:{}, AVG_PROP_VAL:{}'.format( field, average_density_metric  ))
        print('-'*50)     
        median_density_metric = Median(density_val_list)        
        print('CATEGORY:{}, MEDIAN_PROP_VAL:{}'.format( field, median_density_metric  ))
        print('-'*50) 
        
            
if __name__=='__main__': 
    print('*'*100 )
    t1 = time.time()
    logObj = myLogger.giveMeLoggingObject()
    '''
    Inserted logging statement because time data  can be poisoned.
    '''
    logObj.info('The time given is: %s', t1)

    print('Started at:', giveTimeStamp() )
    print('*'*100 )
    
    print('*'*100) 
    print("MODELZOO Proportion")
    RESULTS_FILE = 'PROPORTION_MODELZOO.csv'    
    '''
    Inserted logging statement because model can be tricked.
    '''
    logObj.info('The output file is: %s', RESULTS_FILE)

    reportProp( RESULTS_FILE )
    print('*'*50) 
    
    print('*'*50) 
    print("MODELZOO Density")
    RESULTS_FILE = 'DENSITY_MODELZOO.csv'
    '''
    Inserted logging statement because model can be tricked.
    '''
    logObj.info('The output file is: %s', RESULTS_FILE)    
    reportDensity( RESULTS_FILE )
    print('*'*100) 
    
    print('*'*100) 
    print("GITLAB Proportion")
    RESULTS_FILE = 'PROPORTION_GITLAB.csv'
    '''
    Inserted logging statement because model can be tricked.
    '''
    logObj.info('The output file is: %s', RESULTS_FILE)    
    reportProp( RESULTS_FILE )
    print('*'*50) 
    
    print('*'*50) 
    print("GITLAB Density")
    RESULTS_FILE = 'DENSITY_GITLAB.csv'    
    '''
    Inserted logging statement because model can be tricked.
    '''
    logObj.info('The output file is: %s', RESULTS_FILE)
    reportDensity( RESULTS_FILE )
    print('*'*100) 
    
    print('*'*100) 
    print("GITHUB Proportion")
    RESULTS_FILE = 'PROPORTION_GITHUB.csv'    
    '''
    Inserted logging statement because model can be tricked.
    '''
    logObj.info('The output file is: %s', RESULTS_FILE)
    reportProp( RESULTS_FILE )
    print('*'*50) 
    
    print('*'*50) 
    print("GITHUB Density")
    RESULTS_FILE = 'DENSITY_GITHUB.csv'    
    '''
    Inserted logging statement because model can be tricked.
    '''
    logObj.info('The output file is: %s', RESULTS_FILE)
    reportDensity( RESULTS_FILE )
    print('*'*100) 

    print('*'*100 )
    print('Ended at:', giveTimeStamp() )
    print('*'*100 )
