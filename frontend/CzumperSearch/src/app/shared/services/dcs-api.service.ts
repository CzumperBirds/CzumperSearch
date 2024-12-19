import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { DcsApiResponse } from '../interfaces/dcsApiResponse.model';

@Injectable({
  providedIn: 'root'
})
export class DcsApiService {
  private baseUrl: string = 'https://api-test.czumpers.com/api/v1/data-collection';

  private dscStatus : BehaviorSubject<DcsApiResponse> = new BehaviorSubject<DcsApiResponse>(this.getDCServiceStatus());

  constructor(private http: HttpClient) {}

  bindDataSet(): Observable<DcsApiResponse> {
      return this.dscStatus.asObservable();
    }

  getDCServiceStatus() : any {
    const endpoint = `${this.baseUrl}/status`;
    console.log(endpoint)
    let returnData
    let responseData = this.http.get<any>(endpoint);
    responseData.subscribe({
      next: (response) =>  returnData = response,
      error: (error) => console.error('GET Error:', error),
    });
    console.log(returnData)
    return returnData
  }

  postData(body: any): Observable<any> {
    const endpoint = `${this.baseUrl}/control`;
    return this.http.post<any>(endpoint, body);
  }
}
