import pandas as pd
import numpy as np

def transform_orginal(df):
    '''
    Add the splitting of 'MAHARASHTRA' to four different regions.
    '''

    df.loc[df['Location'] == 'BELLARY', 'Location'] =  'BALLARI'
    df['YEAR'] = df['Sown \nDate'].apply(lambda x: x.year)
    df['Sow Month'] = df['Sown \nDate'].apply(lambda x: x.month)

    cluster_dict = {0:'3', 1:'4', 2:'1', 3:'', 4:'2'}

    for i in range(5):
        #df2.loc[df2['Village'].values in vil_names[i], 'Location'] = 'MAHARASHTRA'+ cluster_dict[i]
        df['Location'] = df['Village'].apply(lambda x:
                                              ('MAHARASHTRA'+ cluster_dict[i])
                                              if x in vil_names[i] else
                                              df[df['Village'] == x]['Location'].values[0],
                                              0)

    return df

#AFTER transform_orginal(), THE DATAFRAME HAS COLUMNS YEAR AND SOW MONTH. THE DF
#ALSO HAS 4 EXTRA LOCATIONS, NAMELY MAHARASHTRA1, MAHARASHTRA2...

def merge_transform(df, rainfall_df, altitude_df):
    '''
    '''

    rain_org_df = pd.merge(df, rainfall_df, on=['Location', 'YEAR'])

    rain_org_df['Rainfall'] = rain_org_df.apply(lambda x:
                                                (x[str(x['Sow Month'])] +
                                                 x[str(x['Sow Month'] + 1)] +
                                                 x[str(x['Sow Month'] + 2)])

                                                if x['Sow Month'] < 11
                                                else

                                                (x[str(x['Sow Month'])] +
                                                x[str(x['Sow Month'] + 1)] +
                                                6.05)

                                                if x['Sow Month'] < 12
                                                else

                                                (x[str(x['Sow Month'])] + 7.05),
                                                 axis=1)

    final_df = pd.merge(rain_org_df, altitude_df, on=['Location'])

    return final_df

#AFTER merge_transform, THE DATAFRAME HAS BEEN MERGED WITH RAINFALL AND ALTITUDE
#THE RAINFALL HAS BEEN CALCULATED AND MERGED ON LOCATION AND YEAR, THE ALT IS
# MERGED ON JUST LOCATION.
