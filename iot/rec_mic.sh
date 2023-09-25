output_file="audio/output.mp4a"
termux-microphone-record -l 10 -f $output_file

echo "aws s3 cp $(pwd)/$output_file $BUCKET/iot/$output_file"
aws s3 cp $(pwd)/$output_file $BUCKET/iot/$output_file
rm -r $output_file
