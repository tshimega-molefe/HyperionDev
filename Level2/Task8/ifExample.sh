#!/bin/bash

# Check if one of the folders is named "new_folder"
for dir in */; do
    if [[ "$dir" == "new_folder/" ]]; then
        # Create a new folder called "if_folder"
        mkdir if_folder
        echo "if_folder folder created."

        # Check if "if_folder" exists and create "hyperionDev" or "new-projects"
        if [[ -d "if_folder" ]]; then
            # "if_folder" exists, create "hyperionDev"
            mkdir hyperionDev
            echo "hyperionDev folder created."
        else
            # "if_folder" doesn't exist, create "new-projects"
            mkdir new-projects
            echo "new-projects folder created."
        fi
        break
    fi
done
