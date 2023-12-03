#! /bin/bash
source_directory="./starter"
target_directory="./solutions/year_$1/day_$(printf %02d $2)"

if ! [ -d $target_directory ]
then
    mkdir -p $target_directory
else
    echo "The directory for this puzzle already exists."
    exit 1
fi

for file in "$source_directory"/*; do
    if [[ -f $file ]]; then
        cp $file $target_directory
    fi
done
