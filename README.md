# DiabetesPrediction
Pre-requisites:
   pickle file(pip install pickle-mixin)
   numpy
   streamlit for deployment(pip install streamlit)
Step 1:   
In order to Open the trained model(.sav file),use the following instructions:
    import pickle
    pickle.load(open("<file-directory>","rb") #here for file path we need to change backward slash as forward slash
    #because the code is dumped in pickle file in binary format
Step 2:
Streamlit installation:
Run the following commands in terminal one by one
  pip install streamlit
  streamlit hello
Step 3:
After streamlit installation for run DiabetesPredictionWebApp,run the following command in terminal 
   streamlit run <file-directory>
  
  
               
