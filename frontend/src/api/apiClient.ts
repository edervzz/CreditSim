import axios from "axios";
import type { MessagesResponseDto } from "./MessagesResponse.dto";

const basepath = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

export type ResultPost<T>= {
    ok: boolean;
    resultData?: T;
    messages?: MessagesResponseDto;
}

const httpClient = axios.create({
    baseURL: basepath
});

export async function _CallPost<TRequest, TResponse>(url: string, inputData?: TRequest): Promise<ResultPost<TResponse>>{
    try {        
        const response = await httpClient.post<TResponse>(url, inputData);
        
        return {
            ok: true,
            resultData: response.data
        };
    } catch (error) {
        if (axios.isAxiosError(error)){
            return {
                ok: false,
                messages: (error.response?.data as MessagesResponseDto) ?? { messages: [{ code: "UNKNOWN", message: error.message }] }
            }
        }
        return {
            ok: false,
            messages: {messages: [{ code: "UNKNOWN", message: String(error) }]}
        };
    }
}