import pandas as pd

#pd.set_option('display.max_columns', 10)
pd.set_option('display.expand_frame_repr', False)


def main():
	#data_csv_frame = pd.read_csv("bank_branches.csv");
	url="https://raw.githubusercontent.com/snarayanank2/indian_banks/master/bank_branches.csv"
	data_csv_frame = pd.read_csv(url);
	#print(data_csv_frame);
	input_value(data_csv_frame);

def input_value(data_csv_frame):
	val_check=input('\nEnter 1 to find bank details by IFSC OR 2 to find all bank details by bank name and city AND 0 to exit: ');
	#print(val_check);
	if (val_check==1):
   		bank_dtls_ifsc(data_csv_frame);
   	elif(val_check==2):
   		all_bank_dtls(data_csv_frame)
   	elif(val_check==0):
   		print("OK.. Bye")
	else:
   		print("Try Again");

  
def bank_dtls_ifsc(data_csv_frame):
	ifsc_code=raw_input("Enter 11 digit IFSC Code: ");
	if (len(ifsc_code)==11):
		ifsc_code=ifsc_code.upper();
		bank_full_data=data_csv_frame[data_csv_frame["ifsc"] == ifsc_code];
		if (len(bank_full_data)==1):
			bank_full_data_final =  pd.DataFrame(bank_full_data);
			print("\nIFSC CODE: "+bank_full_data_final.iloc[0]['ifsc']);
			print("BANK NAME: "+bank_full_data_final.iloc[0]['bank_name']);
			print("BRANCH: "+bank_full_data_final.iloc[0]['branch']);
			print("CITY: "+bank_full_data_final.iloc[0]['city']);
			print("DISTRICT: "+bank_full_data_final.iloc[0]['district']);
			print("STATE: "+bank_full_data_final.iloc[0]['state']);
			print("ADDRESS: "+bank_full_data_final.iloc[0]['address']);
			#bank_details = [{'IFSC CODE': bank_full_data.iloc[0]['ifsc'] ,'BANK NAME': bank_full_data.iloc[0]['bank_name'],'BRANCH': bank_full_data.iloc[0]['branch'],'CITY': bank_full_data.iloc[0]['city'], 'DISTRICT': bank_full_data.iloc[0]['district'], 'STATE': bank_full_data.iloc[0]['state'], 'ADDRESS' : bank_full_data.iloc[0]['address']}];
			#bank_details =  pd.DataFrame(bank_details);
			#print(bank_details);
		else:
			print("Data not found");
	else:
		print("IFSC not valid format");
	# run_again=input("Enter 1 to check another bank details by ifsc code , 2 to get bank: ");
	# if (run_again==1):
	input_value(data_csv_frame);	
	

def all_bank_dtls(data_csv_frame):

	bank_name=raw_input("Enter Bank Name: ");
	bank_city=raw_input("Enter Bank City: ");
	bank_name=bank_name.upper();
	bank_city=bank_city.upper();

	bank_full_data=data_csv_frame[(data_csv_frame["bank_name"] == bank_name) & (data_csv_frame["city"] == bank_city)];
	bank_full_data_final =  pd.DataFrame(bank_full_data);
	print("Total Bank Found : " + str(len(bank_full_data)));
	#print(bank_full_data_final)
	if (len(bank_full_data)==0):
		print("No Data Found for this entry.")
	else:
		bank_details=[];
		for i in range(0,len(bank_full_data)):
			#print(bank_full_data.iloc[i]['ifsc'],bank_full_data.iloc[i]['branch'])
			bank_details = bank_details+[{'IFSC CODE': bank_full_data.iloc[i]['ifsc'] ,'BANK NAME': bank_full_data.iloc[i]['bank_name'],'BRANCH': bank_full_data.iloc[i]['branch'],'CITY': bank_full_data.iloc[i]['city'], 'DISTRICT': bank_full_data.iloc[i]['district'], 'STATE': bank_full_data.iloc[i]['state'], 'ADDRESS' : bank_full_data.iloc[i]['address']}];
		bank_details =  pd.DataFrame(bank_details);
		print(bank_details);
	input_value(data_csv_frame);


if __name__== "__main__":
  main();

