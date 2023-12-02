output_file="output.mp4a"
termux-microphone-record -l 10 -f $output_file

echo "aws s3 cp $(pwd)/$output_file $BUCKET/iot/$output_file"
aws s3 cp $(pwd)/$output_file $BUCKET/iot/$output_file
rm  $output_file
