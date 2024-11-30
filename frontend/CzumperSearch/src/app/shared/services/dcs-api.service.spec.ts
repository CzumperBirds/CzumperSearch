import { TestBed } from '@angular/core/testing';

import { DcsApiService } from './dcs-api.service';

describe('DcsApiService', () => {
  let service: DcsApiService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DcsApiService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
