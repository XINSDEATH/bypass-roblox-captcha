
import httpx, time, fade

capmonsterkey=''




createTask = httpx.post(            "https://api.capmonster.cloud/createTask", json={
                        "clientKey": capmonsterkey,     "task": {
                            "type": "HCaptchaTaskProxyless",         "websiteURL": "https://roblox.com/login",         "websiteKey":
                            "476068BF-9607-4799-B53D-966BE98E2B81"
                        }
                    }).json()["taskId"]

print(fade.pinkred(f"Captcha Task: {createTask}"))

getResults = {}
getResults["status"] = "processing"
while getResults["status"] == "processing":
                    print("waiting")
                    getResults = httpx.post(                "https://api.capmonster.cloud/getTaskResult",     json={
                            "clientKey": capmonsterkey,         "taskId": createTask
                        }).json()

                    time.sleep(1)

solution = getResults["solution"]#["gRecaptchaResponse"]
print(fade.pinkred(f"Captcha Solved"))
print(solution)
