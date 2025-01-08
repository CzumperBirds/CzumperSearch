import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { DcsApiResponse } from '../interfaces/dcsApiResponse.model';

@Injectable({
  providedIn: 'root'
})
export class DcsApiService {
  private baseUrl: string = 'https://api-test.czumpers.com/api/v1/data-collection';


  constructor(private http: HttpClient) {}

  getDCServiceStatus() : any {
    const endpoint = `${this.baseUrl}/status`;
    console.log(endpoint)
    return this.http.get(endpoint);
  }

  postData(body: any): Observable<any> {
    const endpoint = `${this.baseUrl}/control`;
    return this.http.post<any>(endpoint, body);
  }
}
