def section1_information_collection():
    """
    Section 1: Information Collection
    Collects all necessary information from the user including:
    - Exported WeChat text
    - Text type (GroupText or 2UserText)
    - User names and count
    - Group name (if applicable)
    - Dates in the chat history
    """
    print("=== Section 1: Information Collection ===")
    
    # Step 1: Create a new txt file and allow user to store the exported text
    print("\nStep 1: Creating text file for exported WeChat data")
    print("Please paste your exported WeChat text below.")
    print("When finished, type 'END' on a new line and press Enter:")
    print("-" * 50)
    
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == 'END':
                break
            lines.append(line)
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            return None
    
    exported_text = '\n'.join(lines)
    
    # Save to txt file
    filename = "wechat_export.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(exported_text)
    
    print(f"\n✓ Text saved to {filename}")
    
    # Step 2: Ask for text type and store the type value
    print("\nStep 2: Determining text type")
    print("What type of exported text is this?")
    print("1. GroupText (exported from a group chat)")
    print("2. 2UserText (exported from a private chat between 2 users)")
    
    while True:
        choice = input("Enter your choice (1 or 2): ").strip()
        if choice == '1':
            text_type = "GroupText"
            break
        elif choice == '2':
            text_type = "2UserText"
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
    
    print(f"✓ Text type set to: {text_type}")
    
    # Step 3: Handle user information based on text type
    print(f"\nStep 3: Collecting user information for {text_type}")
    
    if text_type == "2UserText":
        # For 2UserText, store number 2 in variable
        num_users = 2
        print(f"✓ Number of users automatically set to: {num_users}")
        
        # Get the two user names
        user_names = []
        print("Please enter the names of the 2 users in the chat:")
        for i in range(2):
            while True:
                name = input(f"Enter name of user {i+1}: ").strip()
                if name:
                    user_names.append(name)
                    break
                else:
                    print("Name cannot be empty. Please enter a valid name.")
        
        group_name = None  # No group name for 2UserText
        
    else:  # GroupText
        # Ask for number of users and create corresponding list
        print("For group chat, we need to know the number of users.")
        while True:
            try:
                num_users = int(input("Enter the number of users in the group chat: ").strip())
                if num_users > 0:
                    break
                else:
                    print("Number of users must be greater than 0.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Create list for user names with corresponding length
        user_names = []
        print(f"\nPlease enter the names of all {num_users} users sequentially:")
        for i in range(num_users):
            while True:
                name = input(f"Enter name of user {i+1}: ").strip()
                if name:
                    user_names.append(name)
                    break
                else:
                    print("Name cannot be empty. Please enter a valid name.")
        
        # Ask for group chat name
        while True:
            group_name = input("\nEnter the name of the group chat: ").strip()
            if group_name:
                break
            else:
                print("Group name cannot be empty. Please enter a valid name.")
    
    print(f"✓ User names collected: {user_names}")
    if group_name:
        print(f"✓ Group name: {group_name}")
    
    # Step 4: Ask for dates and create list for date storage
    print("\nStep 4: Collecting date information")
    print("How many dates are included in the chat history?")
    while True:
        try:
            num_dates = int(input("Number of dates: ").strip())
            if num_dates > 0:
                break
            else:
                print("Number of dates must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Create list for dates and collect them
    dates = []
    print(f"\nPlease enter all {num_dates} dates.")
    print("Supported formats: YYYY-MM-DD, YYYY-M-DD, YYYY-MM-D, YYYY-M-D")
    print("Example: 2025-5-31 or 2025-05-31")
    
    for i in range(num_dates):
        while True:
            date = input(f"Enter date {i+1}: ").strip()
            if date:
                # Basic validation for date format
                if validate_date_format(date):
                    dates.append(date)
                    break
                else:
                    print("Invalid date format. Please use YYYY-MM-DD, YYYY-M-DD, YYYY-MM-D, or YYYY-M-D")
            else:
                print("Date cannot be empty. Please enter a valid date.")
    
    print(f"✓ Dates collected: {dates}")
    
    # Print the current state of the text file for debugging
    print("\n" + "="*60)
    print("SECTION 1 COMPLETED - CURRENT TEXT CONTENT:")
    print("="*60)
    with open(filename, 'r', encoding='utf-8') as f:
        current_text = f.read()
    print(current_text)
    print("="*60)
    print("END OF CURRENT TEXT CONTENT")
    print("="*60)
    
    # Return all collected information
    collected_info = {
        'filename': filename,
        'text_type': text_type,
        'num_users': num_users,
        'user_names': user_names,
        'group_name': group_name,
        'dates': dates,
        'exported_text': exported_text
    }
    
    print("\n✓ Section 1 completed successfully!")
    print("✓ All information collected and stored.")
    
    return collected_info


def validate_date_format(date_str):
    """
    Validates if the date string matches the required formats:
    YYYY-MM-DD, YYYY-M-DD, YYYY-MM-D, YYYY-M-D
    """
    import re
    
    # Pattern for YYYY-M-D or YYYY-MM-DD and combinations
    pattern = r'^\d{4}-\d{1,2}-\d{1,2}$'
    
    if re.match(pattern, date_str):
        try:
            parts = date_str.split('-')
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
            
            # Basic range validation
            if 1000 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31:
                return True
        except (ValueError, IndexError):
            pass
    
    return False


# Test function for Section 1
def test_section1():
    """
    Test function to run Section 1 independently
    """
    print("Testing Section 1: Information Collection")
    print("="*50)
    
    try:
        info = section1_information_collection()
        if info:
            print("\nTest completed successfully!")
            print("Collected information summary:")
            for key, value in info.items():
                if key != 'exported_text':  # Don't print the full text again
                    print(f"  {key}: {value}")
        else:
            print("\nTest was cancelled or failed.")
    except Exception as e:
        print(f"\nError during testing: {e}")

def section2_simple_processing(collected_info):
    """
    Section 2: Simple Processing
    Removes unnecessary parts from the exported WeChat text:
    1. Remove easily identifiable unnecessary parts ('Dear:', '发自我的 iPad')
    2. Remove chat history headers based on text type
    3. Remove date separators
    """
    print("=== Section 2: Simple Processing ===")
    
    filename = collected_info['filename']
    text_type = collected_info['text_type']
    user_names = collected_info['user_names']
    group_name = collected_info['group_name']
    dates = collected_info['dates']
    
    # Read current text from file
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print("Starting simple processing...")
    
    # Step 1: Remove easily identifiable unnecessary parts
    print("\nStep 1: Removing easily identifiable unnecessary parts")
    
    # Remove 'Dear:'
    text = text.replace('Dear:', '')
    print("✓ Removed 'Dear:'")
    
    # Remove '发自我的 iPad'
    text = text.replace('发自我的 iPad', '')
    print("✓ Removed '发自我的 iPad'")
    
    # Clean up extra whitespace and empty lines created by removals
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:  # Only keep non-empty lines
            cleaned_lines.append(stripped_line)
    text = '\n'.join(cleaned_lines)
    
    # Print current state after step 1
    print("\n" + "-"*50)
    print("TEXT AFTER STEP 1:")
    print("-"*50)
    print(text)
    print("-"*50)
    
    # Step 2: Remove sophisticated parts based on text type
    print("\nStep 2: Removing sophisticated parts based on text type")
    
    if text_type == "GroupText":
        # Build string: '微信群"' + group_name + '"的聊天记录如下:'
        group_header = f'微信群"{group_name}"的聊天记录如下:'
        text = text.replace(group_header, '')
        print(f"✓ Removed GroupText header: '{group_header}'")
        
    else:  # 2UserText
        # Build string: '"' + first_user + '"和"' + second_user + '"的聊天记录如下:'
        user_header = f'"{user_names[0]}"和"{user_names[1]}"的聊天记录如下:'
        text = text.replace(user_header, '')
        print(f"✓ Removed 2UserText header: '{user_header}'")
    
    # Clean up extra whitespace and empty lines created by removals
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:  # Only keep non-empty lines
            cleaned_lines.append(stripped_line)
    text = '\n'.join(cleaned_lines)
    
    # Print current state after step 2
    print("\n" + "-"*50)
    print("TEXT AFTER STEP 2:")
    print("-"*50)
    print(text)
    print("-"*50)
    
    # Step 3: Remove date separators
    print("\nStep 3: Removing date separators")
    
    for date in dates:
        # Build string: '—————  ' + date + '  —————'
        date_separator = f'—————  {date}  —————'
        text = text.replace(date_separator, '')
        print(f"✓ Removed date separator: '{date_separator}'")
    
    # Clean up extra whitespace and empty lines created by removals
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:  # Only keep non-empty lines
            cleaned_lines.append(stripped_line)
    text = '\n'.join(cleaned_lines)
    
    # Print current state after step 3
    print("\n" + "-"*50)
    print("TEXT AFTER STEP 3:")
    print("-"*50)
    print(text)
    print("-"*50)
    
    # Save the processed text back to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"\n✓ Processed text saved to {filename}")
    
    # Final output for section 2
    print("\n" + "="*60)
    print("SECTION 2 COMPLETED - CURRENT TEXT CONTENT:")
    print("="*60)
    print(text)
    print("="*60)
    print("END OF CURRENT TEXT CONTENT")
    print("="*60)
    
    # Update collected_info with processed text
    collected_info['exported_text'] = text
    
    print("\n✓ Section 2 completed successfully!")
    print("✓ Simple processing finished.")
    
    return collected_info


def validate_date_format(date_str):
    """
    Validates if the date string matches the required formats:
    YYYY-MM-DD, YYYY-M-DD, YYYY-MM-D, YYYY-M-D
    """
    import re
    
    # Pattern for YYYY-M-D or YYYY-MM-DD and combinations
    pattern = r'^\d{4}-\d{1,2}-\d{1,2}$'
    
    if re.match(pattern, date_str):
        try:
            parts = date_str.split('-')
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
            
            # Basic range validation
            if 1000 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31:
                return True
        except (ValueError, IndexError):
            pass
    
    return False


def section3_sophisticated_processing(collected_info):
    """
    Section 3: Sophisticated Processing
    Replaces real user names with censored names (Speaker1:, Speaker2:, etc.)
    1. Start iteration through each username from user list
    2. Generate censored names based on position in list (Speaker1, Speaker2, etc.)
    3. Add ':' to create FinalizedCensoredNames (Speaker1:, Speaker2:, etc.)
    4. Replace all real names with FinalizedCensoredNames in the text
    5. Continue iteration until all names are replaced
    """
    print("=== Section 3: Sophisticated Processing ===")
    
    filename = collected_info['filename']
    user_names = collected_info['user_names']
    
    # Read current text from file
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print("Starting sophisticated processing...")
    print(f"Real user names to be replaced: {user_names}")
    
    # Step 1-3: Generate censored names and FinalizedCensoredNames
    print("\nStep 1-3: Generating censored names and FinalizedCensoredNames")
    
    finalized_censored_names = []
    
    # Start iteration where we select each username from the name list
    for i, real_name in enumerate(user_names):
        # Generate censored name based on position (Speaker1, Speaker2, etc.)
        censored_name = f"Speaker{i+1}"
        
        # Add ':' to become FinalizedCensoredName
        finalized_censored_name = f"{censored_name}:"
        finalized_censored_names.append(finalized_censored_name)
        
        print(f"✓ Position {i+1}: '{real_name}' → '{censored_name}' → '{finalized_censored_name}'")
    
    print(f"✓ All FinalizedCensoredNames created: {finalized_censored_names}")
    
    # Step 4-5: Replace real names with FinalizedCensoredNames in iteration
    print("\nStep 4-5: Replacing real names with FinalizedCensoredNames")
    
    # Sort user names by length (longest first) to avoid partial replacements
    name_mapping = list(zip(user_names, finalized_censored_names))
    name_mapping.sort(key=lambda x: len(x[0]), reverse=True)
    
    print("Replacement order (longest names first to avoid partial matches):")
    for real_name, finalized_censored_name in name_mapping:
        print(f"  '{real_name}' → '{finalized_censored_name}'")
    
    # Continue iteration until all names have been replaced
    for real_name, finalized_censored_name in name_mapping:
        # Replace real name with FinalizedCensoredName in the text
        occurrences_before = text.count(real_name)
        if occurrences_before > 0:
            text = text.replace(real_name, finalized_censored_name)
            occurrences_after = text.count(real_name)
            replaced_count = occurrences_before - occurrences_after
            print(f"✓ Replaced '{real_name}' with '{finalized_censored_name}' ({replaced_count} occurrences)")
        else:
            print(f"⚠ No occurrences of '{real_name}' found in text")
    
    # Clean up any potential formatting issues
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:  # Only keep non-empty lines
            cleaned_lines.append(stripped_line)
    text = '\n'.join(cleaned_lines)
    
    # Save the processed text back to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"\n✓ Processed text saved to {filename}")
    
    # Final output for section 3
    print("\n" + "="*60)
    print("SECTION 3 COMPLETED - CURRENT TEXT CONTENT:")
    print("="*60)
    print(text)
    print("="*60)
    print("END OF CURRENT TEXT CONTENT")
    print("="*60)
    
    # Update collected_info with processed text and finalized censored names
    collected_info['exported_text'] = text
    collected_info['finalized_censored_names'] = finalized_censored_names
    
    print("\n✓ Section 3 completed successfully!")
    print("✓ Sophisticated processing finished.")
    print(f"✓ FinalizedCensoredNames stored for future sections: {finalized_censored_names}")
    
    return collected_info


def validate_date_format(date_str):
    """
    Validates if the date string matches the required formats:
    YYYY-MM-DD, YYYY-M-DD, YYYY-MM-D, YYYY-M-D
    """
    import re
    
    # Pattern for YYYY-M-D or YYYY-MM-DD and combinations
    pattern = r'^\d{4}-\d{1,2}-\d{1,2}$'
    
    if re.match(pattern, date_str):
        try:
            parts = date_str.split('-')
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
            
            # Basic range validation
            if 1000 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31:
                return True
        except (ValueError, IndexError):
            pass
    
    return False

def identify_and_remove_time_patterns(text):
    """
    Function that identifies time terms such as 'HH:MM' where HH is the hour 
    in 24-hour system and MM is the minute in 60-minute system.
    
    The function works by traversing through the currently modified string 
    and identifies each character. If a character is a number, the code notes 
    it and its index and checks whether this number and other four characters 
    before it reveal a 'number-number-colon-number-number' pattern.
    
    Only starts identifying the pattern at and after the 5th character of the 
    string to avoid 'Out of indexes Error'.
    """
    print("Running time pattern identification and removal function...")
    
    # Convert text to list for easier manipulation
    text_chars = list(text)
    removed_patterns = []
    
    # Start from 5th character (index 4) to avoid index errors
    i = 4  # 5th character position
    
    while i < len(text_chars):
        # Check if current character is a number
        if text_chars[i].isdigit():
            # Check if this number and 4 characters before it form HH:MM pattern
            # Pattern: number-number-colon-number-number (current char is last number)
            if (i >= 4 and  # Ensure we have enough characters before
                text_chars[i-4].isdigit() and     # First number (H)
                text_chars[i-3].isdigit() and     # Second number (H)
                text_chars[i-2] == ':' and        # Colon
                text_chars[i-1].isdigit() and     # First number (M)
                text_chars[i].isdigit()):         # Second number (M) - current char
                
                # Extract the time pattern for logging
                time_pattern = ''.join(text_chars[i-4:i+1])
                removed_patterns.append(time_pattern)
                
                # Remove the 5-character time pattern (from i-4 to i inclusive)
                del text_chars[i-4:i+1]
                
                # Adjust index after deletion (move back by 4 positions)
                i = i - 4
                continue
        
        i += 1
    
    # Log removed patterns
    if removed_patterns:
        print(f"✓ Removed {len(removed_patterns)} time patterns: {removed_patterns}")
    else:
        print("✓ No time patterns found to remove")
    
    return ''.join(text_chars)

def section4_time_removal(collected_info):
    """
    Section 4: Time Removal
    Removes time terms such as 'HH:MM' from the currently processed text:
    1. Build function that identifies time patterns using specified algorithm
    2. Function only starts identifying patterns from 5th character to avoid errors
    3. Run the function to remove all time terms from the text
    """
    print("=== Section 4: Time Removal ===")
    
    filename = collected_info['filename']
    
    # Read current text from file
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print("Starting time removal processing...")
    print(f"Text length before time removal: {len(text)} characters")
    
    # Print current state before time removal
    print("\n" + "-"*50)
    print("TEXT BEFORE TIME REMOVAL:")
    print("-"*50)
    print(text)
    print("-"*50)
    
    # Step 1-3: Build and run the time pattern removal function
    print("\nStep 1-3: Building and running time pattern identification function")
    
    # Run the time pattern removal function
    text_after_time_removal = identify_and_remove_time_patterns(text)
    
    print(f"Text length after time removal: {len(text_after_time_removal)} characters")
    
    # Clean up any potential formatting issues created by time removal
    lines = text_after_time_removal.split('\n')
    cleaned_lines = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:  # Only keep non-empty lines
            cleaned_lines.append(stripped_line)
    text_after_time_removal = '\n'.join(cleaned_lines)
    
    # Print current state after time removal
    print("\n" + "-"*50)
    print("TEXT AFTER TIME REMOVAL:")
    print("-"*50)
    print(text_after_time_removal)
    print("-"*50)
    
    # Save the processed text back to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text_after_time_removal)
    
    print(f"\n✓ Processed text saved to {filename}")
    
    # Final output for section 4
    print("\n" + "="*60)
    print("SECTION 4 COMPLETED - CURRENT TEXT CONTENT:")
    print("="*60)
    print(text_after_time_removal)
    print("="*60)
    print("END OF CURRENT TEXT CONTENT")
    print("="*60)
    
    # Update collected_info with processed text
    collected_info['exported_text'] = text_after_time_removal
    
    print("\n✓ Section 4 completed successfully!")
    print("✓ Time removal processing finished.")
    
    return collected_info


def validate_date_format(date_str):
    """
    Validates if the date string matches the required formats:
    YYYY-MM-DD, YYYY-M-DD, YYYY-MM-D, YYYY-M-D
    """
    import re
    
    # Pattern for YYYY-M-D or YYYY-MM-DD and combinations
    pattern = r'^\d{4}-\d{1,2}-\d{1,2}$'
    
    if re.match(pattern, date_str):
        try:
            parts = date_str.split('-')
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
            
            # Basic range validation
            if 1000 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31:
                return True
        except (ValueError, IndexError):
            pass
    
    return False

def section5_full_stop_check(collected_info):
    """
    Section 5: Full Stop Sign Check (Updated)
    1. First traverse: Identify SpeakerHeading and SentenceSaid lines, combine them
    2. Second traverse: Add Chinese full stop periods to lines without them
    
    Process:
    - SpeakerHeading: lines that are just "SpeakerX:" (FinalizedCensoredName)
    - SentenceSaid: lines that contain actual sentence content
    - Append SentenceSaid to their corresponding SpeakerHeading
    - Add Chinese full stops to lines that don't have them
    """
    print("=== Section 5: Full Stop Sign Check ===")
    
    filename = collected_info['filename']
    finalized_censored_names = collected_info['finalized_censored_names']
    
    # Read current text from file
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print("Starting full stop sign check processing...")
    
    # Print current state before processing
    print("\n" + "-"*50)
    print("TEXT BEFORE FULL STOP CHECK:")
    print("-"*50)
    print(text)
    print("-"*50)
    
    # Step 1: First traverse - identify and combine SpeakerHeading and SentenceSaid lines
    print("\nStep 1: First traverse - identifying and combining SpeakerHeading and SentenceSaid lines")
    
    lines = text.split('\n')
    processed_lines = []
    sentence_appends = 0
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if line:  # Only process non-empty lines
            # Check if this line is a SpeakerHeading (just "SpeakerX:" with no content after)
            is_speaker_heading = False
            for censored_name in finalized_censored_names:
                if line == censored_name:  # Exact match to "SpeakerX:"
                    is_speaker_heading = True
                    break
            
            if is_speaker_heading:
                # This is a SpeakerHeading, look for the next SentenceSaid line
                current_speaker_line = line
                
                # Look for the next non-empty line as potential SentenceSaid
                j = i + 1
                while j < len(lines):
                    next_line = lines[j].strip()
                    if next_line:  # Found non-empty line
                        # Check if this next line is NOT another SpeakerHeading
                        is_next_speaker = False
                        for censored_name in finalized_censored_names:
                            if next_line == censored_name or next_line.startswith(censored_name.replace(':', '') + ':'):
                                is_next_speaker = True
                                break
                        
                        if not is_next_speaker:
                            # This is SentenceSaid, append it to current speaker
                            combined_line = f"{current_speaker_line} {next_line}"
                            processed_lines.append(combined_line)
                            sentence_appends += 1
                            print(f"✓ Combined: '{current_speaker_line}' + '{next_line}' → '{combined_line}'")
                            i = j + 1  # Skip the sentence line we just processed
                            break
                        else:
                            # Next line is another speaker, so current speaker has no content
                            processed_lines.append(current_speaker_line)
                            print(f"✓ SpeakerHeading with no content: '{current_speaker_line}'")
                            i = i + 1
                            break
                    j += 1
                else:
                    # Reached end of lines, current speaker has no content
                    processed_lines.append(current_speaker_line)
                    print(f"✓ SpeakerHeading with no content: '{current_speaker_line}'")
                    i = i + 1
            else:
                # This line is not a standalone SpeakerHeading
                # Check if it already contains speaker content (SpeakerX: content)
                contains_speaker = False
                for censored_name in finalized_censored_names:
                    if line.startswith(censored_name):
                        contains_speaker = True
                        break
                
                if contains_speaker:
                    # Line already has speaker and content combined
                    processed_lines.append(line)
                    print(f"✓ Already combined: '{line}'")
                else:
                    # This is a standalone sentence without speaker (shouldn't happen after previous sections)
                    processed_lines.append(line)
                    print(f"⚠ Standalone sentence: '{line}'")
                
                i += 1
        else:
            # Skip empty lines
            i += 1
    
    print(f"\n✓ Completed first traverse: {sentence_appends} SentenceSaid lines appended to SpeakerHeading lines")
    
    # Create text after first traverse
    text_after_first_traverse = '\n'.join(processed_lines)
    
    # Print current state after first traverse
    print("\n" + "-"*50)
    print("TEXT AFTER FIRST TRAVERSE:")
    print("-"*50)
    print(text_after_first_traverse)
    print("-"*50)
    
    # Step 2: Second traverse - add Chinese full stop periods
    print("\nStep 2: Second traverse - adding Chinese full stop periods to lines without them")
    
    final_lines = []
    full_stops_added = 0
    
    for line in processed_lines:
        if line.strip():  # Only process non-empty lines
            if not line.endswith('。'):
                # Add Chinese full stop
                new_line = f"{line}。"
                final_lines.append(new_line)
                full_stops_added += 1
                print(f"✓ Added full stop: '{line}' → '{new_line}'")
            else:
                # Line already has full stop
                final_lines.append(line)
                print(f"✓ Already has full stop: '{line}'")
    
    print(f"\n✓ Completed second traverse: {full_stops_added} Chinese full stops added")
    
    # Create final text
    text_after_full_stop_check = '\n'.join(final_lines)
    
    # Print current state after second traverse
    print("\n" + "-"*50)
    print("TEXT AFTER SECOND TRAVERSE:")
    print("-"*50)
    print(text_after_full_stop_check)
    print("-"*50)
    
    # Save the processed text back to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text_after_full_stop_check)
    
    print(f"\n✓ Processed text saved to {filename}")
    
    # Final output for section 5
    print("\n" + "="*60)
    print("SECTION 5 COMPLETED - CURRENT TEXT CONTENT:")
    print("="*60)
    print(text_after_full_stop_check)
    print("="*60)
    print("END OF CURRENT TEXT CONTENT")
    print("="*60)
    
    # Update collected_info with processed text
    collected_info['exported_text'] = text_after_full_stop_check
    
    print("\n✓ Section 5 completed successfully!")
    print("✓ Full stop sign check processing finished.")
    print(f"✓ {sentence_appends} lines combined, {full_stops_added} full stops added")
    
    return collected_info


def validate_date_format(date_str):
    """
    Validates if the date string matches the required formats:
    YYYY-MM-DD, YYYY-M-DD, YYYY-MM-D, YYYY-M-D
    """
    import re
    
    # Pattern for YYYY-M-D or YYYY-MM-DD and combinations
    pattern = r'^\d{4}-\d{1,2}-\d{1,2}$'
    
    if re.match(pattern, date_str):
        try:
            parts = date_str.split('-')
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
            
            # Basic range validation
            if 1000 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31:
                return True
        except (ValueError, IndexError):
            pass
    
    return False

def section6_chat_history_simplification(collected_info):
    """
    Section 6: Chat History Simplification
    Combines successive discourses from the same person into one line:
    1. Traverse text and identify FinalizedCensoredNames and their indexes
    2. If current speaker index is same as previous, combine content
    3. Continue until all successive discourses are combined
    
    Process:
    - Identify FinalizedCensoredName in each line and get its index
    - If index matches previous line's index, combine content
    - Remove redundant FinalizedCensoredName from successive lines
    """
    print("=== Section 6: Chat History Simplification ===")
    
    filename = collected_info['filename']
    finalized_censored_names = collected_info['finalized_censored_names']
    
    # Read current text from file
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print("Starting chat history simplification processing...")
    print(f"FinalizedCensoredNames to identify: {finalized_censored_names}")
    
    # Print current state before processing
    print("\n" + "-"*50)
    print("TEXT BEFORE CHAT HISTORY SIMPLIFICATION:")
    print("-"*50)
    print(text)
    print("-"*50)
    
    # Step 1-3: Traverse text and combine successive discourses
    print("\nStep 1-3: Traversing text and combining successive discourses from same speakers")
    
    lines = text.split('\n')
    simplified_lines = []
    last_speaker_index = -1  # Initialize to -1 to indicate no previous speaker
    combinations_made = 0
    
    for line_num, line in enumerate(lines):
        line = line.strip()
        if not line:  # Skip empty lines
            continue
        
        # Step 1: Identify FinalizedCensoredName in current line and get its index
        current_speaker_index = -1
        current_speaker_name = None
        
        for i, censored_name in enumerate(finalized_censored_names):
            if line.startswith(censored_name):
                current_speaker_index = i
                current_speaker_name = censored_name
                break
        
        if current_speaker_index == -1:
            # Line doesn't start with any FinalizedCensoredName (shouldn't happen after previous sections)
            simplified_lines.append(line)
            print(f"⚠ Line {line_num+1} doesn't start with FinalizedCensoredName: '{line}'")
            last_speaker_index = -1
            continue
        
        print(f"✓ Line {line_num+1}: Found '{current_speaker_name}' (index {current_speaker_index})")
        
        # Step 2: Judge whether index is same as last one detected
        if current_speaker_index == last_speaker_index and simplified_lines:
            # Same speaker as previous line - combine content
            # Extract content after the speaker name from current line
            content_after_speaker = line[len(current_speaker_name):].strip()
            
            if content_after_speaker:  # Only combine if there's actual content
                # Append content to the last line in simplified_lines
                simplified_lines[-1] = simplified_lines[-1] + content_after_speaker
                combinations_made += 1
                print(f"✓ Combined with previous line: '{content_after_speaker}' → '{simplified_lines[-1]}'")
            else:
                # No content after speaker name, just skip this line
                print(f"✓ Skipped empty speaker line: '{line}'")
        else:
            # Different speaker or first line - add as new line
            simplified_lines.append(line)
            print(f"✓ Added new speaker line: '{line}'")
            last_speaker_index = current_speaker_index
    
    print(f"\n✓ Completed simplification: {combinations_made} line combinations made")
    
    # Create simplified text
    text_after_simplification = '\n'.join(simplified_lines)
    
    # Print current state after simplification
    print("\n" + "-"*50)
    print("TEXT AFTER CHAT HISTORY SIMPLIFICATION:")
    print("-"*50)
    print(text_after_simplification)
    print("-"*50)
    
    # Save the processed text back to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text_after_simplification)
    
    print(f"\n✓ Processed text saved to {filename}")
    
    # Final output for section 6
    print("\n" + "="*60)
    print("SECTION 6 COMPLETED - CURRENT TEXT CONTENT:")
    print("="*60)
    print(text_after_simplification)
    print("="*60)
    print("END OF CURRENT TEXT CONTENT")
    print("="*60)
    
    # Update collected_info with processed text
    collected_info['exported_text'] = text_after_simplification
    
    print("\n✓ Section 6 completed successfully!")
    print("✓ Chat history simplification processing finished.")
    print(f"✓ {combinations_made} successive discourse combinations made")
    
    return collected_info


def validate_date_format(date_str):
    """
    Validates if the date string matches the required formats:
    YYYY-MM-DD, YYYY-M-DD, YYYY-MM-D, YYYY-M-D
    """
    import re
    
    # Pattern for YYYY-M-D or YYYY-MM-DD and combinations
    pattern = r'^\d{4}-\d{1,2}-\d{1,2}$'
    
    if re.match(pattern, date_str):
        try:
            parts = date_str.split('-')
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
            
            # Basic range validation
            if 1000 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31:
                return True
        except (ValueError, IndexError):
            pass
    
    return False


def test_section1():
    """
    Test function to run Section 1 independently
    """
    print("Testing Section 1: Information Collection")
    print("="*50)
    
    try:
        info = section1_information_collection()
        if info:
            print("\nTest completed successfully!")
            print("Collected information summary:")
            for key, value in info.items():
                if key != 'exported_text':  # Don't print the full text again
                    print(f"  {key}: {value}")
        else:
            print("\nTest was cancelled or failed.")
        return info
    except Exception as e:
        print(f"\nError during testing: {e}")
        return None


def test_section2():
    """
    Test function to run Section 2 independently
    """
    print("Testing Section 2: Simple Processing")
    print("="*50)
    
    try:
        # First run Section 1 to get the collected info
        info = section1_information_collection()
        if info:
            print("\nSection 1 completed. Now running Section 2...")
            processed_info = section2_simple_processing(info)
            if processed_info:
                print("\nSection 2 test completed successfully!")
                return processed_info
            else:
                print("\nSection 2 test failed.")
                return None
        else:
            print("\nSection 1 failed. Cannot proceed to Section 2.")
            return None
    except Exception as e:
        print(f"\nError during testing: {e}")
        return None


def test_section3():
    """
    Test function to run Section 3 independently
    """
    print("Testing Section 3: Sophisticated Processing")
    print("="*50)
    
    try:
        # First run Sections 1 and 2 to get the collected info
        info = section1_information_collection()
        if info:
            print("\nSection 1 completed. Now running Section 2...")
            processed_info = section2_simple_processing(info)
            if processed_info:
                print("\nSection 2 completed. Now running Section 3...")
                final_info = section3_sophisticated_processing(processed_info)
                if final_info:
                    print("\nSection 3 test completed successfully!")
                    return final_info
                else:
                    print("\nSection 3 test failed.")
                    return None
            else:
                print("\nSection 2 failed. Cannot proceed to Section 3.")
                return None
        else:
            print("\nSection 1 failed. Cannot proceed.")
            return None
    except Exception as e:
        print(f"\nError during testing: {e}")
        return None


def test_section4():
    """
    Test function to run Section 4 independently
    """
    print("Testing Section 4: Time Removal")
    print("="*50)
    
    try:
        # First run Sections 1, 2, and 3 to get the collected info
        info = section1_information_collection()
        if info:
            print("\nSection 1 completed. Now running Section 2...")
            processed_info = section2_simple_processing(info)
            if processed_info:
                print("\nSection 2 completed. Now running Section 3...")
                further_info = section3_sophisticated_processing(processed_info)
                if further_info:
                    print("\nSection 3 completed. Now running Section 4...")
                    final_info = section4_time_removal(further_info)
                    if final_info:
                        print("\nSection 4 test completed successfully!")
                        return final_info
                    else:
                        print("\nSection 4 test failed.")
                        return None
                else:
                    print("\nSection 3 failed. Cannot proceed to Section 4.")
                    return None
            else:
                print("\nSection 2 failed. Cannot proceed to Section 3.")
                return None
        else:
            print("\nSection 1 failed. Cannot proceed.")
            return None
    except Exception as e:
        print(f"\nError during testing: {e}")
        return None


def test_section5():
    """
    Test function to run Section 5 independently
    """
    print("Testing Section 5: Full Stop Sign Check")
    print("="*50)
    
    try:
        # First run Sections 1, 2, 3, and 4 to get the collected info
        info = section1_information_collection()
        if info:
            print("\nSection 1 completed. Now running Section 2...")
            processed_info = section2_simple_processing(info)
            if processed_info:
                print("\nSection 2 completed. Now running Section 3...")
                further_info = section3_sophisticated_processing(processed_info)
                if further_info:
                    print("\nSection 3 completed. Now running Section 4...")
                    more_info = section4_time_removal(further_info)
                    if more_info:
                        print("\nSection 4 completed. Now running Section 5...")
                        final_info = section5_full_stop_check(more_info)
                        if final_info:
                            print("\nSection 5 test completed successfully!")
                            return final_info
                        else:
                            print("\nSection 5 test failed.")
                            return None
                    else:
                        print("\nSection 4 failed. Cannot proceed to Section 5.")
                        return None
                else:
                    print("\nSection 3 failed. Cannot proceed to Section 4.")
                    return None
            else:
                print("\nSection 2 failed. Cannot proceed to Section 3.")
                return None
        else:
            print("\nSection 1 failed. Cannot proceed.")
            return None
    except Exception as e:
        print(f"\nError during testing: {e}")
        return None


def test_section6():
    """
    Test function to run Section 6 independently
    """
    print("Testing Section 6: Chat History Simplification")
    print("="*50)
    
    try:
        # First run Sections 1, 2, 3, 4, and 5 to get the collected info
        info = section1_information_collection()
        if info:
            print("\nSection 1 completed. Now running Section 2...")
            processed_info = section2_simple_processing(info)
            if processed_info:
                print("\nSection 2 completed. Now running Section 3...")
                further_info = section3_sophisticated_processing(processed_info)
                if further_info:
                    print("\nSection 3 completed. Now running Section 4...")
                    more_info = section4_time_removal(further_info)
                    if more_info:
                        print("\nSection 4 completed. Now running Section 5...")
                        even_more_info = section5_full_stop_check(more_info)
                        if even_more_info:
                            print("\nSection 5 completed. Now running Section 6...")
                            final_info = section6_chat_history_simplification(even_more_info)
                            if final_info:
                                print("\nSection 6 test completed successfully!")
                                return final_info
                            else:
                                print("\nSection 6 test failed.")
                                return None
                        else:
                            print("\nSection 5 failed. Cannot proceed to Section 6.")
                            return None
                    else:
                        print("\nSection 4 failed. Cannot proceed to Section 5.")
                        return None
                else:
                    print("\nSection 3 failed. Cannot proceed to Section 4.")
                    return None
            else:
                print("\nSection 2 failed. Cannot proceed to Section 3.")
                return None
        else:
            print("\nSection 1 failed. Cannot proceed.")
            return None
    except Exception as e:
        print(f"\nError during testing: {e}")
        return None


def test_sections_1_and_2():
    """
    Test function to run both Section 1 and Section 2 together
    """
    print("Testing Sections 1 and 2 Combined")
    print("="*60)
    
    try:
        # Run Section 1
        print("Running Section 1...")
        info = section1_information_collection()
        
        if info:
            print("\n" + "="*60)
            print("Section 1 completed successfully! Now running Section 2...")
            print("="*60)
            
            # Run Section 2
            processed_info = section2_simple_processing(info)
            
            if processed_info:
                print("\n" + "="*60)
                print("BOTH SECTIONS COMPLETED SUCCESSFULLY!")
                print("="*60)
                print("Final processed information summary:")
                for key, value in processed_info.items():
                    if key != 'exported_text':  # Don't print the full text again
                        print(f"  {key}: {value}")
                return processed_info
            else:
                print("\nSection 2 failed.")
                return None
        else:
            print("\nSection 1 failed. Cannot proceed.")
            return None
    except Exception as e:
        print(f"\nError during testing: {e}")
        return None


def test_sections_1_2_and_3():
    """
    Test function to run Sections 1, 2, and 3 together
    """
    print("Testing Sections 1, 2, and 3 Combined")
    print("="*70)
    
    try:
        # Run Section 1
        print("Running Section 1...")
        info = section1_information_collection()
        
        if info:
            print("\n" + "="*70)
            print("Section 1 completed successfully! Now running Section 2...")
            print("="*70)
            
            # Run Section 2
            processed_info = section2_simple_processing(info)
            
            if processed_info:
                print("\n" + "="*70)
                print("Section 2 completed successfully! Now running Section 3...")
                print("="*70)
                
                # Run Section 3
                final_info = section3_sophisticated_processing(processed_info)
                
                if final_info:
                    print("\n" + "="*70)
                    print("ALL THREE SECTIONS COMPLETED SUCCESSFULLY!")
                    print("="*70)
                    print("Final processed information summary:")
                    for key, value in final_info.items():
                        if key != 'exported_text':  # Don't print the full text again
                            print(f"  {key}: {value}")
                    return final_info
                else:
                    print("\nSection 3 failed.")
                    return None
            else:
                print("\nSection 2 failed.")
                return None
        else:
            print("\nSection 1 failed. Cannot proceed.")
            return None
    except Exception as e:
        print(f"\nError during testing: {e}")
        return None


def test_sections_1_2_3_and_4():
    """
    Test function to run Sections 1, 2, 3, and 4 together
    """
    print("Testing Sections 1, 2, 3, and 4 Combined")
    print("="*75)
    
    try:
        # Run Section 1
        print("Running Section 1...")
        info = section1_information_collection()
        
        if info:
            print("\n" + "="*75)
            print("Section 1 completed successfully! Now running Section 2...")
            print("="*75)
            
            # Run Section 2
            processed_info = section2_simple_processing(info)
            
            if processed_info:
                print("\n" + "="*75)
                print("Section 2 completed successfully! Now running Section 3...")
                print("="*75)
                
                # Run Section 3
                further_info = section3_sophisticated_processing(processed_info)
                
                if further_info:
                    print("\n" + "="*75)
                    print("Section 3 completed successfully! Now running Section 4...")
                    print("="*75)
                    
                    # Run Section 4
                    final_info = section4_time_removal(further_info)
                    
                    if final_info:
                        print("\n" + "="*75)
                        print("ALL FOUR SECTIONS COMPLETED SUCCESSFULLY!")
                        print("="*75)
                        print("Final processed information summary:")
                        for key, value in final_info.items():
                            if key != 'exported_text':  # Don't print the full text again
                                print(f"  {key}: {value}")
                        return final_info
                    else:
                        print("\nSection 4 failed.")
                        return None
                else:
                    print("\nSection 3 failed.")
                    return None
            else:
                print("\nSection 2 failed.")
                return None
        else:
            print("\nSection 1 failed. Cannot proceed.")
            return None
    except Exception as e:
        print(f"\nError during testing: {e}")
        return None


def test_sections_1_2_3_4_and_5():
    """
    Test function to run Sections 1, 2, 3, 4, and 5 together
    """
    print("Testing Sections 1, 2, 3, 4, and 5 Combined")
    print("="*80)
    
    try:
        # Run Section 1
        print("Running Section 1...")
        info = section1_information_collection()
        
        if info:
            print("\n" + "="*80)
            print("Section 1 completed successfully! Now running Section 2...")
            print("="*80)
            
            # Run Section 2
            processed_info = section2_simple_processing(info)
            
            if processed_info:
                print("\n" + "="*80)
                print("Section 2 completed successfully! Now running Section 3...")
                print("="*80)
                
                # Run Section 3
                further_info = section3_sophisticated_processing(processed_info)
                
                if further_info:
                    print("\n" + "="*80)
                    print("Section 3 completed successfully! Now running Section 4...")
                    print("="*80)
                    
                    # Run Section 4
                    more_info = section4_time_removal(further_info)
                    
                    if more_info:
                        print("\n" + "="*80)
                        print("Section 4 completed successfully! Now running Section 5...")
                        print("="*80)
                        
                        # Run Section 5
                        final_info = section5_full_stop_check(more_info)
                        
                        if final_info:
                            print("\n" + "="*80)
                            print("ALL FIVE SECTIONS COMPLETED SUCCESSFULLY!")
                            print("="*80)
                            print("Final processed information summary:")
                            for key, value in final_info.items():
                                if key != 'exported_text':  # Don't print the full text again
                                    print(f"  {key}: {value}")
                            return final_info
                        else:
                            print("\nSection 5 failed.")
                            return None
                    else:
                        print("\nSection 4 failed.")
                        return None
                else:
                    print("\nSection 3 failed.")
                    return None
            else:
                print("\nSection 2 failed.")
                return None
        else:
            print("\nSection 1 failed. Cannot proceed.")
            return None
    except Exception as e:
        print(f"\nError during testing: {e}")
        return None


def test_sections_1_2_3_4_5_and_6():
    """
    Test function to run Sections 1, 2, 3, 4, 5, and 6 together
    """
    print("Testing Sections 1, 2, 3, 4, 5, and 6 Combined")
    print("="*85)
    
    try:
        # Run Section 1
        print("Running Section 1...")
        info = section1_information_collection()
        
        if info:
            print("\n" + "="*85)
            print("Section 1 completed successfully! Now running Section 2...")
            print("="*85)
            
            # Run Section 2
            processed_info = section2_simple_processing(info)
            
            if processed_info:
                print("\n" + "="*85)
                print("Section 2 completed successfully! Now running Section 3...")
                print("="*85)
                
                # Run Section 3
                further_info = section3_sophisticated_processing(processed_info)
                
                if further_info:
                    print("\n" + "="*85)
                    print("Section 3 completed successfully! Now running Section 4...")
                    print("="*85)
                    
                    # Run Section 4
                    more_info = section4_time_removal(further_info)
                    
                    if more_info:
                        print("\n" + "="*85)
                        print("Section 4 completed successfully! Now running Section 5...")
                        print("="*85)
                        
                        # Run Section 5
                        even_more_info = section5_full_stop_check(more_info)
                        
                        if even_more_info:
                            print("\n" + "="*85)
                            print("Section 5 completed successfully! Now running Section 6...")
                            print("="*85)
                            
                            # Run Section 6
                            final_info = section6_chat_history_simplification(even_more_info)
                            
                            if final_info:
                                print("\n" + "="*85)
                                print("ALL SIX SECTIONS COMPLETED SUCCESSFULLY!")
                                print("="*85)
                                print("Final processed information summary:")
                                for key, value in final_info.items():
                                    if key != 'exported_text':  # Don't print the full text again
                                        print(f"  {key}: {value}")
                                return final_info
                            else:
                                print("\nSection 6 failed.")
                                return None
                        else:
                            print("\nSection 5 failed.")
                            return None
                    else:
                        print("\nSection 4 failed.")
                        return None
                else:
                    print("\nSection 3 failed.")
                    return None
            else:
                print("\nSection 2 failed.")
                return None
        else:
            print("\nSection 1 failed. Cannot proceed.")
            return None
    except Exception as e:
        print(f"\nError during testing: {e}")
        return None


# Main execution
if __name__ == "__main__":
    # Run all six sections together
    test_sections_1_2_3_4_5_and_6()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    