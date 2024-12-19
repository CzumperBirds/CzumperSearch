import { Component, OnInit } from '@angular/core';
import { DcsApiService } from '../../services/dcs-api.service';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { Subscription } from 'rxjs';
import { DcsApiResponse } from '../../interfaces/dcsApiResponse.model';

@Component({
  selector: 'app-arthur-button',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  templateUrl: './arthur-button.component.html',
  styleUrl: './arthur-button.component.scss'
})
export class ArthurButtonComponent implements OnInit{

  private dataSubscription: Subscription | undefined;


  dcServiceStatusResponse : DcsApiResponse = this.DscApi.getDCServiceStatus()

  dcsRunning : boolean = false;
  changeInProgress : boolean = true;
  constructor (private DscApi : DcsApiService){

  }

async  ngOnInit(): Promise<any> {
    this.dataSubscription = this.DscApi.bindDataSet().subscribe((data) => {
      this.dcServiceStatusResponse = data;
    });
      await this.updateStatus()
  }

  ngOnDestroy(): void {
    if (this.dataSubscription) {
      this.dataSubscription.unsubscribe();
    }
  }

  async updateStatus() {
    await this.fetchData()
    this.dcsRunning = this.dcServiceStatusResponse.is_running
  }

  async fetchData() {
    this.dcServiceStatusResponse  = this.DscApi.getDCServiceStatus()
  }

  async switchStatus(status: string){
    this.DscApi.postData({'action': status}).subscribe({
      next: (response) =>  this.dcServiceStatusResponse = response,
      error: (error) => console.error('POST Error:', error),
    });
  }
}
