from requests import get

def download(url, file_name = None):
	if not file_name:
		file_name = url.split('/')[-1]

	with open(file_name, "wb") as file:
            response = get(url)
            file.write(response.content)

if __name__ == '__main__':
	# 아래의 url 변수에 영상 소스 주소를 넣는다.
	url = "https://ABC/abc.mp4"
	download(url)