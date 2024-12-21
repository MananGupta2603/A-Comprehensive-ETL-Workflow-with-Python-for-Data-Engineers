def inches_to_meters(height_in_inches):
    return height_in_inches * 0.0254

def pounds_to_kilograms(weight_in_pounds):
    return weight_in_pounds * 0.453592

def transform_data(data):
    data['Height_m'] = data['height'].apply(inches_to_meters)
    data['Weight_kg'] = data['weight'].apply(pounds_to_kilograms)
    return data
