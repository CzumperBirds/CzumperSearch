import { Component, OnInit } from '@angular/core';
import { DcsApiService } from '../../services/dcs-api.service';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { Subscription, firstValueFrom} from 'rxjs';
import { DcsApiResponse } from '../../interfaces/dcsApiResponse.model';

@Component({
  selector: 'app-arthur-button',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  templateUrl: './arthur-button.component.html',
  styleUrl: './arthur-button.component.scss'
})
export class ArthurButtonComponent implements OnInit{

  dcServiceStatusResponse : DcsApiResponse | undefined;

  dcsRunning : boolean = false;
  initialised : boolean = false;
  changeInProgress : boolean = true;
  constructor (private DcsApi : DcsApiService){

  }

async  ngOnInit(): Promise<any> {
  await this.fetchData()
  }

  ngOnDestroy(): void {
  }

  async fetchData() {
    try {
      this.dcServiceStatusResponse = await firstValueFrom(this.DcsApi.getDCServiceStatus());
      console.log('Data:', this.dcServiceStatusResponse);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      this.initialised = true
    }
  }

  async switchStatus(status: string){
    this.DcsApi.postData({'action': status}).subscribe({
      next: (response) =>  this.dcServiceStatusResponse = response,
      error: (error) => console.error('POST Error:', error),
    });
  }
}
