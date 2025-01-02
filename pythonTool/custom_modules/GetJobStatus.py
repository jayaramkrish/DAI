import requests

def get_job_status(job_url, sslMode, headers=None):
    try:
        response = requests.get(job_url, verify=sslMode, headers=headers)
        if response.status_code == 200:
            job_status = response.json()["result"]
            return job_status
        else:
            return "Failed to get job status. Error code: " + str(response.status_code)
    except requests.exceptions.RequestException as e:
        return "Failed to get job status. Error: " + str(e)
