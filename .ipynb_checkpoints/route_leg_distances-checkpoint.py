def get_route(pickup_lon, pickup_lat, dropoff_lon, dropoff_lat):
    """
    Partition data into train and test sets.

    Parameters
    ----------
    df: A pandas DataFrame to partition
    target: A string specifying the name of the target column
    test_size: (optional) An integer for number of test examples or a float
               for proportion of test examples
    seed: (optional) An integer to set seed for reproducibility

    Returns
    -------
    X_train, X_test, y_train, y_test

    """

    loc = "{},{};{},{}".format(pickup_lon, pickup_lat, dropoff_lon, dropoff_lat)
    url = "http://127.0.0.1:5000/route/v1/driving/"
    r = requests.get(url + loc)
    if r.status_code != 200:
        return {}

    res = r.json()
    routes = polyline.decode(res['routes'][0]['geometry'])
    start_point = [res['waypoints'][0]['location'][1], res['waypoints'][0]['location'][0]]
    end_point = [res['waypoints'][1]['location'][1], res['waypoints'][1]['location'][0]]
    distance = res['routes'][0]['distance']

    out = {'route': routes,
           'start_point': start_point,
           'end_point': end_point,
           'distance': distance
           }

    return out