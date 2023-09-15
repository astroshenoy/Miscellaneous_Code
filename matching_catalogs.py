from astropy.io import fits
import pandas as pd
from astropy.table import Table
from tqdm import tqdm

def match_catalogs(cat1, cat2, common_cols, filename):
    ''' 
    Takes in two catalogs, merges them based on values 
    in common columns and returns the merged catalog
    
    Input parameters:
    cat1        : str, location of catalog 1; file format in csv
    cat 2       : str, path to catalog 2 ;file format in fits/csv
    common_cols : list, the columns that are common in both files 
                    which are used to combine the catalogs e.g., ['FIBERID', 'MJD']
    filename    : str, name of new file to save the merged catalog
    
    Output: Saves the merged file at given location
    '''
    df1 = pd.read_csv(cat1) # if file is in csv fomat
    df2 = Table.read(cat2) # if file is in fits format
    
    # making sure all columns are 1D in both files (e.g, MPAJHU has some multi-dim columns like plug_mag)
    names = [name for name in df1.colnames if len(df1[name].shape) <= 1] 
    df1_new = df1[names].to_pandas()
    names2 = [name for name in df2.colnames if len(df2[name].shape) <= 1] 
    df2_new = df2[names].to_pandas()
    
    common_columns = common_cols
    # Merge the DataFrames based on the common columns
    merged_df = pd.merge(df1_new, df2_new, on=common_columns, how='inner')
    # Save the merged DataFrame
    merged_df.to_csv(filename)
    
    
# E.g.,     
# common_cols = ['PLATEID', 'MJD', 'FIBERID']
# cat1 = "/Users/shravya/Desktop/04_PhD/Raw_catalogs/GSWLC-X2_updated2.csv"
# cat2 = "/Users/shravya/Desktop/04_PhD/Raw_catalogs/MPA-JHU/galSpec_mastercatalog_SFGs_0p04z0p3.fits"
# filename = "/Users/shravya/Desktop/04_PhD/Raw_catalogs/MPAJHU_GSWLC_merged.csv"

# match_catalogs(cat1, cat2, common_cols, filename)