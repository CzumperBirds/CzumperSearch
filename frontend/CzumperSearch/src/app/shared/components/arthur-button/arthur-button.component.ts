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
  imports: [CommonModule],
  templateUrl: './arthur-button.component.html',
  styleUrl: './arthur-button.component.scss'
})
export class ArthurButtonComponent implements OnInit{

  dcServiceStatusResponse : DcsApiResponse = {
    is_running: false
  };
  dcsRunning : boolean = false;

  constructor (private DscApi : DcsApiService){

  }

  ngOnInit(): void {
      this.fetchData()
      this.updateStatus()
  }

  updateStatus(): void {
    this.fetchData()
    this.dcsRunning = this.dcServiceStatusResponse.is_running
  }

  fetchData(): void {
    this.DscApi.getDCServiceStatus().subscribe({
      next: (response) =>  this.dcServiceStatusResponse = response,
      error: (error) => console.error('GET Error:', error),
    });
  }
}
