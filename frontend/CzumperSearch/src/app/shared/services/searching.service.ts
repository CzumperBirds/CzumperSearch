import { Injectable } from '@angular/core';
import { DataInstance } from '../interfaces/dataInstance.model';
import { BehaviorSubject } from 'rxjs';
import { Observable } from 'rxjs';
import { pickupLines } from '../mocks/mockedJokes';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class SearchingService {

  private baseUrl: string = 'https://api-test.czumpers.com/api/v1/search';

  getMockData() {
    return pickupLines
  }

  private foundData : BehaviorSubject<Array<DataInstance>> = new BehaviorSubject<Array<DataInstance>>([]);

  constructor(private http: HttpClient) {
  }

  bindDataSet(): Observable<Array<DataInstance>> {
    return this.foundData.asObservable();
  }


  getSearchData(searchString : string): Observable<any> {
    const endpoint = `${this.baseUrl}?searchPhrase=${searchString}`;
    console.log(endpoint)
    return this.http.get<any>(endpoint);
  }

  getByTags(body: any): Observable<any> {
    const endpoint = `${this.baseUrl}/tags`;
    return this.http.post<any>(endpoint, body);
  }

  searchData(searchString : string){
    console.log('Searching for data')
    this.getSearchData(searchString).subscribe({
      next: (response) =>  this.foundData.next(response),
      error: (error) => console.error('GET Error:', error),
    });
  }

  searchDataByTags(tag : string){
    console.log('Searching for data')
    this.getByTags([tag]).subscribe({
      next: (response) =>  this.foundData.next(response),
      error: (error) => console.error('GET Error:', error),
    });
  }
}
