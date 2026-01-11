import { _CallPost } from ".";
import type { ResultPost } from "./apiClient";
import type { CreditSimulationRequestDto, CreditSimulationResponseDto } from "./CreditSimulation.dto";


export class CreditSimulatorService{
    async Create(data: CreditSimulationRequestDto): Promise<ResultPost<CreditSimulationResponseDto>>{
        const url = "/simulate";

        return await _CallPost<CreditSimulationRequestDto,CreditSimulationResponseDto>(url,data);
    }
}

