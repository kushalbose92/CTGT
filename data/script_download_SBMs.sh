

# Command to download dataset:
#   bash script_download_SBMs.sh


DIR=SBMs/
cd $DIR


FILE=SBM_CLUSTER.zip
if test -f "$FILE"; then
	echo -e "$FILE already downloaded."
else
	echo -e "\ndownloading $FILE..."
	curl https://data.dgl.ai/dataset/benchmarking-gnns/SBM_CLUSTER.zip -o SBM_CLUSTER.zip -J -L -k
fi


FILE=SBM_PATTERN.zip
if test -f "$FILE"; then
	echo -e "$FILE already downloaded."
else
	echo -e "\ndownloading $FILE..."
	curl https://data.dgl.ai/dataset/benchmarking-gnns/SBM_PATTERN.zip -o SBM_PATTERN.zip -J -L -k
fi


