import { Component } from '@angular/core';
import { LogoComponent } from '../../shared/components/logo-component/logo-component.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [LogoComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent {

}
