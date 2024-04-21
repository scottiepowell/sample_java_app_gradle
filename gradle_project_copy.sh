#!/bin/bash

# Define the source directories and files
src_dirs="gradle src"
src_files="build.gradle gradlew gradlew.bat settings.gradle"

# Directory containing the component directories
base_dir="/t/5_repos/sample_java_app_gradle"

# Loop over each component directory and copy the specified directories and files
for component in $base_dir/component_*; do
    if [ -d "$component" ]; then  # Check if it is a directory
        echo "Copying files and directories to $component"
        
        # Copy directories
        for dir in $src_dirs; do
            if [ -d "$base_dir/$dir" ]; then
                cp -r "$base_dir/$dir" "$component/"
            fi
        done
        
        # Copy files
        for file in $src_files; do
            if [ -f "$base_dir/$file" ]; then
                cp "$base_dir/$file" "$component/"
            fi
        done
    fi
done

echo "Copying complete."
