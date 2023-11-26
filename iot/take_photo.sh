termux-camera-photo img/output.jpge
output_file="img/output.jpge"

echo "aws s3 cp $(pwd)/$output_file $BUCKET/iot/$output_file"
aws s3 cp $(pwd)/$output_file $BUCKET/iot/$output_file
rm -r $output_file
