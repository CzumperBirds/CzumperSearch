import { Component, OnInit } from '@angular/core';
import { DcsApiService } from '../../services/dcs-api.service';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';


export interface DcsApiResponse {
  is_running: false
}
@Component({
  selector: 'app-arthur-button',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  templateUrl: './arthur-button.component.html',
  styleUrl: './arthur-button.component.scss'
})
export class ArthurButtonComponent implements OnInit{

  dcServiceStatusResponse : DcsApiResponse = {
    is_running: false
  };
  dcsRunning : boolean = false;
  changeInProgress : boolean = true;
  constructor (private DscApi : DcsApiService){

  }

  ngOnInit(): void {
      this.updateStatus()
  }

  async updateStatus() {
    await this.fetchData()
    this.dcsRunning = this.dcServiceStatusResponse.is_running
  }

  async fetchData() {
    this.DscApi.getDCServiceStatus().subscribe({
      next: (response) =>  this.dcServiceStatusResponse = response,
      error: (error) => console.error('GET Error:', error),
    });
  }

  async switchStatus(status: string){
    this.DscApi.postData({'action': status}).subscribe({
      next: (response) =>  this.dcServiceStatusResponse = response,
      error: (error) => console.error('GET Error:', error),
    });
  }
}
