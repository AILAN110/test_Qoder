import requests
from typing import Dict, Any

def get_user_usage_data(organization_id: str, token: str, startTime:str, endTime:str, user_id: str = None) -> Dict[str, Any]:
    """
    获取用户使用数据
    
    Args:
        organization_id: 组织 ID（如 "67d8e0b9120358055abf****"）
        startTime: 开始时间
        endTime: 结束时间
        user_id: 用户 ID（如 "369:"，实际保留原格式）
        token: x-yunxiao-token 鉴权令牌
    
    Returns:
        响应中的 JSON 数据（字典格式）
    
    Raises:
        requests.exceptions.RequestException: 网络或请求错误
        ValueError: 响应状态码非 200 时抛出，包含错误信息
    """
    base_url = "https://openapi-rdc.aliyuncs.com"
    endpoint = f"/oapi/v1/lingma/organizations/{organization_id}/developerUsage"
    url = base_url + endpoint

    if user_id is None:
        params = {
            "startTime": startTime,
            "endTime": endTime
        }
    else:
        params = {
            "userId": user_id,
            "startTime": startTime,
            "endTime": endTime
        }

    headers = {
        "Content-Type": "application/json",
        "x-yunxiao-token": token
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()  # 触发 4xx/5xx 异常
        return response.json()
    except requests.exceptions.HTTPError as e:
        # 提取响应体中的错误信息（如果有）
        error_detail = response.text if response.text else str(e)
        raise ValueError(f"HTTP {response.status_code}: {error_detail}") from e
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"请求失败: {e}") from e


def get_department_list(organization_id: str, token: str) -> Dict[str, Any]:
    """
    查询部门列表
    
    Args:
        organization_id: 组织 ID（如 "9a2b****5ef1"）
        token: x-yunxiao-token 鉴权令牌
    
    Returns:
        响应中的 JSON 数据（字典格式），包含部门信息
    
    Raises:
        requests.exceptions.RequestException: 网络或请求错误
        ValueError: 响应状态码非 200 时抛出，包含错误信息
    """
    base_url = "https://openapi-rdc.aliyuncs.com"
    endpoint = f"/oapi/v1/platform/organizations/{organization_id}/departments"
    url = base_url + endpoint

    headers = {
        "Content-Type": "application/json",
        "x-yunxiao-token": token
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()  # 触发 4xx/5xx 异常
        return response.json()
    except requests.exceptions.HTTPError as e:
        # 提取响应体中的错误信息（如果有）
        error_detail = response.text if response.text else str(e)
        raise ValueError(f"HTTP {response.status_code}: {error_detail}") from e
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"请求失败: {e}") from e


def get_department_usage(organization_id: str, department_id: str, start_time: str, end_time: str, token: str, page: int = 1, per_page: int = 100) -> Dict[str, Any]:
    """
    获取部门使用情况
    
    Args:
        organization_id: 组织 ID（如 "c7655445-143f-4466-9724-8b371a21****"）
        department_id: 部门 ID（如 "7b58e90a-063f-475b-ad6d-32d1f438****"）
        start_time: 开始时间（格式：YYYY-MM-DD）
        end_time: 结束时间（格式：YYYY-MM-DD）
        token: x-yunxiao-token 鉴权令牌
        page: 页码，默认为1
        per_page: 每页数量，默认为100
    
    Returns:
        响应中的 JSON 数据（字典格式）
    
    Raises:
        requests.exceptions.RequestException: 网络或请求错误
        ValueError: 响应状态码非 200 时抛出，包含错误信息
    """
    base_url = "https://openapi-rdc.aliyuncs.com"
    endpoint = f"/oapi/v1/lingma/organizations/{organization_id}/departmentUsage"
    url = base_url + endpoint

    params = {
        "departmentId": department_id,
        "startTime": start_time,
        "endTime": end_time,
        "page": page,
        "perPage": per_page
    }

    headers = {
        "Content-Type": "application/json",
        "x-yunxiao-token": token
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()  # 触发 4xx/5xx 异常
        return response.json()
    except requests.exceptions.HTTPError as e:
        # 提取响应体中的错误信息（如果有）
        error_detail = response.text if response.text else str(e)
        raise ValueError(f"HTTP {response.status_code}: {error_detail}") from e
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"请求失败: {e}") from e


def get_member_list(organization_id: str, token: str) -> Dict[str, Any]:
    """
    获取所有成员列表信息
    
    Args:
        organization_id: 组织 ID（如 "99d1****71d4"）
        token: x-yunxiao-token 鉴权令牌
    
    Returns:
        响应中的 JSON 数据（字典格式），包含成员信息
    
    Raises:
        requests.exceptions.RequestException: 网络或请求错误
        ValueError: 响应状态码非 200 时抛出，包含错误信息
    """
    base_url = "https://openapi-rdc.aliyuncs.com"
    endpoint = f"/oapi/v1/platform/organizations/{organization_id}/members"
    url = base_url + endpoint

    headers = {
        "Content-Type": "application/json",
        "x-yunxiao-token": token
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()  # 触发 4xx/5xx 异常
        return response.json()
    except requests.exceptions.HTTPError as e:
        # 提取响应体中的错误信息（如果有）
        error_detail = response.text if response.text else str(e)
        raise ValueError(f"HTTP {response.status_code}: {error_detail}") from e
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"请求失败: {e}") from e


# 使用示例
if __name__ == "__main__":
    try:
        result = get_user_usage_data(
            organization_id="669e3631fe5796af90ff11d7",
            token="pt-6ZOzPkUmPBHKeAzmwwg5AInb_30ad5962-5300-4d36-8965-506355a67dd0",
            startTime="2025-05-25",
            endTime="2025-05-26"
        )
        print("请求成功，返回数据：", result)
    except Exception as e:
        print("发生错误：", e)