All of this rep is what they let available at the freelance application, with exception of my run.py script, after running it the script does basically what is asked on the lines below, that contain what client was asking before I could apply ;-;

-------------------------------------------------------------------------------------------------------------------------------

The files for this folder are arranged as follows:
- Data to work on:
img/                    
train.jsonl             
dev_seen.jsonl          
test_seen.jsonl         
dev_unseen.jsonl        
test_unseen.jsonl       

- Sample results:
sample outputs



Run the script and it will read the jsonl files and extract the field to make folders contain images and text file accordingly.

‘label’       : 0=not-hateful, 1=hateful

for example

Read train.jsonl file and make 2 folders:
not_Hateful_train and Hateful_train

And copy the images over the corresponding folder. Then create text with corresponding name and text content. 

