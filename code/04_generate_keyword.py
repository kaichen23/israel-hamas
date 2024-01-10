import pandas as pd
import json
pd.set_option('display.max_rows', None)

TOPIC = "free palestine"
file_path = "{}/article_results_dict.json".format(TOPIC)

with open(file_path, 'r', encoding="utf-8") as json_file:
    results_dict = json.load(json_file)

keyword_dict = {}
for article, results in results_dict.items():
    result_dict = {}
    # Process each string in the list
    for item in results:
        # Split the string into key-value pairs
        key_value_pairs = item.split(', ')

        # Iterate through the key-value pairs
        for pair in key_value_pairs:
            try:
                key, value_str = pair.split(': ')
                value = int(value_str)
            except:
                print(pair)

            # Check if the key is already in the result_dict
            if key in result_dict:
                # If it's already present, update the value by adding to the sum
                result_dict[key][0] += value
                result_dict[key][1] += 1
            else:
                # If it's not present, initialize the key with [value, count]
                result_dict[key] = [value, 1]

    # Calculate the average for each key
    for key, values in result_dict.items():
        total_sum, count = values
        average = total_sum / count
        result_dict[key] = int(average)

    for key, value in result_dict.items():
        # Update the sum and count of values for the current key
        if key in keyword_dict:
            keyword_dict[key] += value
        else:
            keyword_dict[key] = value

df = pd.DataFrame(list(keyword_dict.items()), columns=['Keyword', 'Count'])
df_sorted = df.sort_values(by='Count', ascending=False)
df_sorted = df_sorted.reset_index(drop=True)
# Display the sorted DataFrame
print(df_sorted)

df_sorted.to_csv('{}/{}_keywords_importance.csv'.format(TOPIC, TOPIC), encoding="utf-8")



