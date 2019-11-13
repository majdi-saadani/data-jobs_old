import json
import os

#list all files
class GenerateFiles:
    entries = os.listdir('communications/')
    # for each files we will read the text and we will change the structure of the data to json
    for entry in entries:
        f = open('./communications/'+entry, "r")
        read_data = f.read()

        new = ""
        filename = f'./processed/communication-{{}}.json'.format(read_data.split("|")[0][3:len(read_data)])

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        for data in read_data.split("|"):
            if(len(new) == 0):
               new =  new+str(data.split('=')[:1]) + ':' +str(data.split('=')[1:2])
            else:
               new =  new+','+str(data.split('=')[:1]) + ':' +str(data.split('=')[1:2])

        data_clean =str ('{'+new.replace("[","").replace("]","").replace('"',"")+'}')
        json_string = (json.dumps(eval(data_clean), indent=4))
        with open(filename, 'w') as file:
            file.write(json_string.replace('"',"'"))
    def test_cal():
        print("ko")

    def create_files(event):
        new = ""
        filename = f'./processed/communication-{{}}.json'.format(read_data.split("|")[0][3:len(read_data)])

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        for data in read_data.split("|"):
            if(len(new) == 0):
               new =  new+str(data.split('=')[:1]) + ':' +str(data.split('=')[1:2])
            else:
               new =  new+','+str(data.split('=')[:1]) + ':' +str(data.split('=')[1:2])

        data_clean =str ('{'+new.replace("[","").replace("]","").replace('"',"")+'}')
        json_string = (json.dumps(eval(data_clean), indent=4))
        with open(filename, 'w') as file:
            file.write(json_string.replace('"',"'"))