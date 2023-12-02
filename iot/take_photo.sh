# Use termux-dialog to get input from the user
PersonName=$(termux-dialog text -t "Enter Your Name" | jq -r '.text')
RealAge=$(termux-dialog text -t "Enter Your Age" | jq -r '.text')

termux-camera-photo img/$PersonName-$RealAge.jpg
output_file="img/$PersonName-$RealAge.jpg"

echo "aws s3 cp $(pwd)/$output_file $BUCKET/iot/$output_file"
aws s3 cp $(pwd)/$output_file $BUCKET/iot/$output_file
rm -r $output_file
